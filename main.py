from dotenv import load_dotenv
from summarizer import summarize_text
from page_parser import get_page_text

load_dotenv()

#config
URL = "https://www.collegeboard.org"

def main():
    text = get_page_text(URL)
    summary = summarize_text(text)
    print("\nSummary of Updates:\n")
    print(summary)

if __name__ == "__main__":
    main()
