def fetch_google_ads_data():
    """
    Returns mock Google Ads data for demo/portfolio purposes.
    Replace with real Google Ads API call when live campaigns exist.
    """
    return {
        "summary": {
            "impressions": 18400,
            "clicks": 920,
            "ctr": 5.0,
            "conversions": 38,
            "cost": 410.50,
            "cpc": 0.45,
            "roas": 3.2,
        },
        "top_campaigns": [
            {"name": "Brand Awareness - Goa", "clicks": 420, "conversions": 18, "cost": 180.00},
            {"name": "Lead Gen - SEO Services", "clicks": 310, "conversions": 14, "cost": 145.00},
            {"name": "Retargeting - Website Visitors", "clicks": 190, "conversions": 6, "cost": 85.50},
        ],
        "note": "Demo data — connect live Google Ads account to replace."
    }