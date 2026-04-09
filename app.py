def generate_email(name, purpose):
    email = f"""
Hi {name},

I hope you are doing well.

I am writing this email regarding {purpose}. I would like to discuss this further and explore possible next steps.

Please let me know a convenient time to connect.

Thank you,
Your Name
"""
    return email


if __name__ == "__main__":
    name = input("Enter recipient name: ")
    purpose = input("Enter purpose of email: ")

    result = generate_email(name, purpose)

    print("\nGenerated Email:\n")
    print(result)