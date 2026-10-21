from crewai import Agent, Task, Crew

# Ask the user for a city
city = input("Which city? ")

# 1. Define the Travel Planner Agent
planner = Agent(
    role="Expert Travel Planner",
    goal="Provide concise, curated, and practical travel recommendations for {city}.",
    backstory=(
        "You are a seasoned globetrotter and local guide who has explored hundreds of "
        "destinations worldwide. You value efficiency and authentic experiences, "
        "ensuring travelers get straight to the best spots without fluff."
    ),
    verbose=True
)

# 2. Define the Task for the Agent
task = Task(
    description=(
        "Find exactly 3 must-visit places in {city}. "
        "Provide a short, punchy description and a practical tip for each location."
    ),
    expected_output=(
        "A clean, numbered list of exactly 3 places in the city. "
        "Each entry must include the name of the place, a brief description, "
        "and a practical tip, with no introductory or concluding paragraphs."
    ),
    agent=planner
)

# 3. Assemble the Crew
crew = Crew(
    agents=[planner],
    tasks=[task],
    verbose=True
)

# 4. Run the Crew and print the result
result = crew.kickoff(inputs={"city": city})
print("\n=== Travel Recommendations ===")
print(result)