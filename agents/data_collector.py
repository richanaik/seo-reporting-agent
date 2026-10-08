from tools.ga4_tool import fetch_ga4_data
from tools.gsc_tool import fetch_gsc_data
from tools.google_ads_tool import fetch_google_ads_data

def data_collector_agent(state: dict) -> dict:
    """
    Agent 1: Pulls data from GA4, GSC, and Google Ads.
    Adds raw data to the shared pipeline state.
    """
    print("🔍 Data Collector Agent running...")

    property_id = state["ga4_property_id"]
    site_url = state["gsc_site_url"]

    print("  → Fetching GA4 data...")
    ga4_data = fetch_ga4_data(property_id)

    print("  → Fetching GSC data...")
    gsc_data = fetch_gsc_data(site_url)

    print("  → Fetching Google Ads data...")
    ads_data = fetch_google_ads_data()

    print("✅ Data collection complete.")

    return {
        **state,
        "ga4_data": ga4_data,
        "gsc_data": gsc_data,
        "ads_data": ads_data,
    }