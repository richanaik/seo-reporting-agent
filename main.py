from dotenv import load_dotenv
from graph import build_graph

load_dotenv()

def run_report(client_name: str, ga4_property_id: str, gsc_site_url: str):
    """
    Run the full SEO reporting pipeline.
    
    Args:
        client_name: Your client's name (appears in the report)
        ga4_property_id: Found in GA4 → Admin → Property Settings (numbers only)
        gsc_site_url: Exact URL as registered in GSC e.g. https://yoursite.com/
    """

    print("\n🚀 Starting SEO Reporting Agent...")
    print(f"   Client: {client_name}")
    print(f"   GA4 Property ID: {ga4_property_id}")
    print(f"   GSC Site URL: {gsc_site_url}")
    print("-" * 50)

    # Initial state
    initial_state = {
        "client_name": client_name,
        "ga4_property_id": ga4_property_id,
        "gsc_site_url": gsc_site_url,
        "ga4_data": None,
        "gsc_data": None,
        "ads_data": None,
        "anomalies": [],
        "insights": [],
        "report_text": "",
        "report_file": "",
    }

    # Run the pipeline
    graph = build_graph()
    final_state = graph.invoke(initial_state)

    print("-" * 50)
    print(f"\n✅ Pipeline complete!")
    print(f"📄 Report saved to: {final_state['report_file']}")
    print(f"\n--- REPORT PREVIEW ---\n")
    print(final_state["report_text"])

if __name__ == "__main__":
    run_report(
        client_name="Richa Naik Portfolio",
        ga4_property_id="556192199",      # ← replace this
        gsc_site_url="https://richa-portfolio-ochre.vercel.app/",      # ← replace this
    )