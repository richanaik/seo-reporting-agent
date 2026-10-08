def anomaly_detector_agent(state: dict) -> dict:
    """
    Agent 2: Compares metrics, detects anomalies, tags severity.
    Threshold: flag anything that changed more than 20%.
    """
    print("🔎 Anomaly Detector Agent running...")

    ga4_data = state["ga4_data"]
    gsc_data = state["gsc_data"]
    ads_data = state["ads_data"]

    anomalies = []
    insights = []

    # --- GA4 Analysis ---
    if len(ga4_data) >= 2:
        # Split into two halves: recent vs previous
        mid = len(ga4_data) // 2
        recent = ga4_data[mid:]
        previous = ga4_data[:mid]

        def avg(data, key):
            values = [row[key] for row in data if row[key] is not None]
            return sum(values) / len(values) if values else 0

        metrics_to_check = [
            ("sessions", "Sessions", "higher is better"),
            ("active_users", "Active Users", "higher is better"),
            ("bounce_rate", "Bounce Rate", "lower is better"),
            ("conversions", "Conversions", "higher is better"),
        ]

        for key, label, direction in metrics_to_check:
            recent_avg = avg(recent, key)
            prev_avg = avg(previous, key)

            if prev_avg == 0:
                continue

            change_pct = ((recent_avg - prev_avg) / prev_avg) * 100

            is_bad = (
                (direction == "higher is better" and change_pct < -20) or
                (direction == "lower is better" and change_pct > 20)
            )
            is_good = (
                (direction == "higher is better" and change_pct > 20) or
                (direction == "lower is better" and change_pct < -20)
            )

            if is_bad:
                anomalies.append({
                    "source": "GA4",
                    "metric": label,
                    "change_pct": round(change_pct, 1),
                    "severity": "high" if abs(change_pct) > 40 else "medium",
                    "direction": "decline",
                    "recent_avg": round(recent_avg, 2),
                    "prev_avg": round(prev_avg, 2),
                })
            elif is_good:
                insights.append({
                    "source": "GA4",
                    "metric": label,
                    "change_pct": round(change_pct, 1),
                    "direction": "improvement",
                    "recent_avg": round(recent_avg, 2),
                    "prev_avg": round(prev_avg, 2),
                })

    # --- GSC Analysis ---
    if gsc_data:
        total_clicks = sum(r["clicks"] for r in gsc_data)
        total_impressions = sum(r["impressions"] for r in gsc_data)
        avg_position = sum(r["position"] for r in gsc_data) / len(gsc_data)
        avg_ctr = sum(r["ctr"] for r in gsc_data) / len(gsc_data)

        insights.append({
            "source": "GSC",
            "metric": "Search Summary",
            "total_clicks": total_clicks,
            "total_impressions": total_impressions,
            "avg_position": round(avg_position, 1),
            "avg_ctr": round(avg_ctr, 2),
            "top_queries": gsc_data[:5],
        })

    # --- Google Ads Analysis ---
    ads_summary = ads_data.get("summary", {})
    if ads_summary:
        insights.append({
            "source": "Google Ads",
            "metric": "Ads Summary",
            "data": ads_summary,
            "top_campaigns": ads_data.get("top_campaigns", []),
            "note": ads_data.get("note", ""),
        })

    print(f"  → Found {len(anomalies)} anomalies, {len(insights)} insights.")
    print("✅ Anomaly detection complete.")

    return {
        **state,
        "anomalies": anomalies,
        "insights": insights,
    }