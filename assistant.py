import os
import sys

try:
    from google import genai
    from google.genai import errors
except ImportError:
    print("⚠️  Required library 'google-genai' is not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 50)
    print("  🤖  Gemini CLI Assistant")
    print("  Type your message and press Enter.")
    print("  Type 'exit' or press Enter on empty input to quit.")
    print("=" * 50)
    print()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("⚠️  GEMINI_API_KEY not set.")
        print("Please set it as an environment variable or via .env file.")
        print("Example: export GEMINI_API_KEY=\"your-key-here\"")
        sys.exit(1)

    try:
        client = genai.Client(api_key=api_key)
        chat = client.chats.create(model="gemini-3.5-flash")
    except Exception as e:
        print(f"⚠️  Failed to initialize Gemini Client: {e}")
        sys.exit(1)

    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit'] or not user_input:
                print("👋 Goodbye!")
                break

            print("Gemini: ", end="", flush=True)

            try:
                response = chat.send_message_stream(user_input)
                for chunk in response:
                    print(chunk.text, end="", flush=True)
                print("\n")
            except errors.ClientError as ce:
                print(f"\n⚠️  Client Error (4xx): {ce}")
            except errors.ServerError as se:
                print(f"\n⚠️  Server Error (5xx): {se}. Please try again shortly.")
            except errors.APIError as ae:
                print(f"\n⚠️  API Error: {ae}")
            except Exception as e:
                print(f"\n⚠️  Connection Error: {e}. Check your connection.")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except EOFError:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
