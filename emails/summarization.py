# summarization.py
import openai

def generate_summary(content):
    openai.api_key = 'YOUR_OPENAI_API_KEY'

    prompt = f"Summarize the following email content:\n{content}"
    
    response = openai.Completion.create(
        engine="davinci-codex",  # You can adjust the engine as needed
        prompt=prompt,
        max_tokens=50  # Adjust the length of the summary
    )

    summary = response.choices[0].text.strip()
    return summary

# Example usage
if __name__ == "__main__":
    email_content = "This is the content of an email that needs summarization. It has important information..."
    summary = generate_summary(email_content)
    print("Generated Summary:", summary)
