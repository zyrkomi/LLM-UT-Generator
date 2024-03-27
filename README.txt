This Flask application leverages an LLM API (OpenAI or "meta/codellama-70b") to automatically generate unit tests for your Python functions.

Installation and Setup

    Create and activate a virtual environment:
        python -m venv venv
        source venv/bin/activate  # Linux/macOS
        venv\Scripts\activate.bat  # Windows

    Install dependencies (inside virtual environment):
        pip install -r requirements.txt

    Set API Key (inside virtual environment):
        Create an account with your chosen LLM provider (OpenAI or Codex) and obtain your API key.
        Recomended: https://build.nvidia.com/explore/discover

            export API_KEY=YOUR_API_KEY  # Linux/macOS
            setx API_KEY=YOUR_API_KEY  # Windows (Command Prompt)

    Running the Application:
        Start the development server:
            python app.py

    Access the application in your web browser at http://localhost:5000 (default port).

    The application provides a form where you can paste your Python function code and submit it.
    You'll receive the generated unit tests on the same page.


Example Usage

    The application accepts Python function code as input and generates unit tests for it. Here are some examples:

    FizzBuzz Function:

        Prompt:

            def fizzbuzz(number):
                if number % 15 == 0:
                    return "FizzBuzz"
                elif number % 3 == 0:
                    return "Fizz"
                elif number % 5 == 0:
                    return "Buzz"
                else:
                    return number

        Generated Tests (may vary):

            def test_fizzbuzz_multiple_of_15():
                assert fizzbuzz(15) == "FizzBuzz"

            def test_fizzbuzz_multiple_of_3():
                assert fizzbuzz(9) == "Fizz"

            def test_fizzbuzz_multiple_of_5():
                assert fizzbuzz(10) == "Buzz"

            def test_fizzbuzz_not_multiple_of_3_or_5():
                assert fizzbuzz(11) == 11



