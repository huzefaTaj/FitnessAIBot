#!/usr/bin/env python3
"""
Setup script for Fitness AI Q&A API
This script helps you configure your OpenAI API key
"""

import os
import sys

def setup_api_key():
    """Interactive setup for OpenAI API key"""
    print("🤖 Fitness AI Q&A API Setup")
    print("=" * 40)
    
    # Check if API key is already set
    current_key = os.getenv("OPENAI_API_KEY")
    if current_key:
        print(f"✅ OpenAI API key is already configured")
        print(f"   Key: {current_key[:8]}...{current_key[-4:]}")
        return True
    
    print("❌ OpenAI API key not found")
    print("\nTo use this API, you need an OpenAI API key.")
    print("You can get one from: https://platform.openai.com/api-keys")
    print("\nOptions:")
    print("1. Set environment variable (recommended for production)")
    print("2. Enter key temporarily (for testing)")
    print("3. Skip for now")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\nTo set the environment variable permanently:")
        print("Windows (PowerShell):")
        print("  [Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'your-key-here', 'User')")
        print("\nWindows (Command Prompt):")
        print("  setx OPENAI_API_KEY your-key-here")
        print("\nLinux/Mac:")
        print("  export OPENAI_API_KEY=your-key-here")
        print("  echo 'export OPENAI_API_KEY=your-key-here' >> ~/.bashrc")
        
    elif choice == "2":
        api_key = input("\nEnter your OpenAI API key: ").strip()
        if api_key.startswith("sk-"):
            # Set for current session
            os.environ["OPENAI_API_KEY"] = api_key
            print("✅ API key set for current session")
            print("Note: This will only work for the current terminal session")
            return True
        else:
            print("❌ Invalid API key format. Should start with 'sk-'")
            return False
    
    elif choice == "3":
        print("⚠️  API will not work without an API key")
        return False
    
    else:
        print("❌ Invalid choice")
        return False

def main():
    """Main setup function"""
    try:
        success = setup_api_key()
        
        if success:
            print("\n🎉 Setup complete!")
            print("You can now run: python main.py")
        else:
            print("\n⚠️  Setup incomplete")
            print("You'll need to configure the API key before using the API")
        
        print("\nFor more information, see README.md")
        
    except KeyboardInterrupt:
        print("\n\nSetup cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
