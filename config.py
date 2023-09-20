# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Gary Vaynerchuk": {
        "objectives": [
            "Expand VeeFreinds Kids Toy and Book Offerings"
        ],
        "tasks": [
            "Identify the largest kid toy and book markets and creat plan to expand to those markets"
        ]
    },
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Gary Vaynerchuk"