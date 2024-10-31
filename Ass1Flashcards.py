# flashcard_app.py
import streamlit as st

# Quiz data for Module 1 and Module 2
quiz_data = [
    # Module 1 questions
    {
        "question": "How do we typically approach building influence diagrams?",
        "options": [
            "Starting from the output and working backwards.",
            "Starting from the inputs and working forwards.",
            "Starting from key midpoints and working outwards."
        ],
        "answer": "Starting from the output and working backwards."
    },
    {
        "question": "Which statement best describes a feature of a good influence diagram?",
        "options": [
            "All cells must be arranged in a circular pattern to ensure feedback loops.",
            "The diagram should contain more decision nodes than outcome nodes.",
            "You should be able to explain how to calculate each cell’s value based only on the cells pointing to it.",
            "Each cell must be connected directly to every other cell in the diagram."
        ],
        "answer": "You should be able to explain how to calculate each cell’s value based only on the cells pointing to it."
    },
    {
        "question": "What’s wrong with this influence diagram?",
        "options": [
            "The diagram should indicate that 'Total Revenue' is directly dependent on the 'Total Costs.'",
            "The diagram should have a direct connection between the selling price per unit and the total costs.",
            "The diagram should have a connection from planned sales to total costs. You cannot calculate total cost from the variable cost per unit and fixed cost only.",
            "The diagram should include a node for 'Net Profit Margin' instead of just 'Profit.'",
            "The diagram should show that the total fixed costs are dependent on the total variable costs."
        ],
        "answer": "The diagram should have a connection from planned sales to total costs. You cannot calculate total cost from the variable cost per unit and fixed cost only."
    },
    {
        "question": "Which is NOT a general principle to follow when creating a model sketch in spreadsheets?",
        "options": [
            "Ensure that all calculations and formulas are placed directly in the input cells to avoid confusion.",
            "Decide key milestone cells that you can treat as submodels and locate a module for them.",
            "Gather all the inputs and decide where to locate them (usually top left).",
            "Determine where the key output of the model should be located (usually bottom right)."
        ],
        "answer": "Ensure that all calculations and formulas are placed directly in the input cells to avoid confusion."
    },
    {
        "question": "Use the tips I shared in the video to debug it to regain the correct $69,662.10 annual operating profit. Describe the error that you needed to fix.",
        "options": [
            "The advertising budget for Q3 was mistakenly entered as $15,000 instead of $10,000, resulting in inflated total expenses.",
            "In the overhead calculations, the reference to the sales revenue was locked to Q1’s value and did not correctly fill across for Q2-Q4’s values.",
            "In the unit sales calculations, the reference forgot to lock a reference leading to references to empty cells.",
            "In the sales revenue calculations, the reference to Unit Sales for Q2 was mistakenly linked to Q1’s value, leading to an incorrect revenue calculation.",
            "In the COGS calculations, the reference to the cost per unit was linked to an incorrect cell, causing it to be overestimated."
        ],
        "answer": "In the overhead calculations, the reference to the sales revenue was locked to Q1’s value and did not correctly fill across for Q2-Q4’s values."
    },
    {
        "question": "Although it doesn’t affect the spreadsheet’s ability to obtain $69,662.10, what is NOT 'best practice' about the highlighted cells below?",
        "options": [
            "These values are inputs because they are numbers that the user must provide, not formulas – they should be moved to the inputs module and only linked here.",
            "The highlighted cells should have been left as formulas rather than converting them to inputs.",
            "The values in the highlighted cells should be converted to percentages for better clarity.",
            "The highlighted cells should have been deleted altogether because sales expenses do not belong in that part of the spreadsheet.",
            "The values should be color-coded to match the rest of the spreadsheet – they should be green."
        ],
        "answer": "These values are inputs because they are numbers that the user must provide, not formulas – they should be moved to the inputs module and only linked here."
    },
    {
        "question": "How might you change the highlighted portion of the model to better match the business situation?",
        "options": [
            "A better model would allow for different advertising budgets for different quarters besides equal increments of $10,000.",
            "A better model would automatically equally divide the advertising budget across all quarters without considering the impact of seasonality or market demand.",
            "A better model would enforce that the advertising budget is fixed for the entire year and cannot be adjusted based on quarterly needs.",
            "A better model would increase the total budget by $10,000 for each subsequent quarter, regardless of performance metrics or market conditions.",
            "A better model would reduce the budget increment by $10,000 each quarter to account for diminishing returns on advertising expenditure."
        ],
        "answer": "A better model would allow for different advertising budgets for different quarters besides equal increments of $10,000."
    },
    {
        "question": "What practice in Python corresponds to the best practice in Excel that you should not 'hard code' numbers into formulas?",
        "options": [
            "In Python models, you should convert all numbers to binary and store them as comments in your code.",
            "In Python models, you should always hard code numbers directly into your formulas for better readability.",
            "In Python models, you should store numerical values as an input parameter at the top instead of embedded into formulas later on.",
            "In Python, it’s best to use string literals in place of numbers to avoid confusion.",
            "In Python models, you should store all numerical values inside your loops to ensure they are recalculated every time."
        ],
        "answer": "In Python models, you should store numerical values as an input parameter at the top instead of embedded into formulas later on."
    },

    # Module 2 questions
    {
        "question": "Given what scenario analysis accomplishes, which of the graphs below would make the most sense to present the results in a presentation?",
        "options": [
            "A stacked bar graph showing how the inputs combine to generate the output.",
            "A bar graph comparing the total after-tax profit under each of the input scenarios.",
            "A scatterplot comparing different input values for each scenario",
            "A line graph with the input variable names on the x-axis and their corresponding input values on the y-axis sorted from greatest to smallest.",
            "A histogram showing the distribution of after-tax profits resulting from randomly generated input values."
        ],
        "answer": "A bar graph comparing the total after-tax profit under each of the input scenarios."
    },
    {
        "question": "How does the line graph depict 'sensitivity analysis'?",
        "options": [
            "The line's convexity or concavity tells you whether or not the model is sensitive to errors in the calculations.",
            "The line graph shows how the output (on the y-axis) changes as you vary the input of interest (on the x-axis).",
            "The line’s shape evokes different moods depending on how sensitive a person the user is.",
            "The line morphs into different shapes to show how sensitive it is to changes in the model assumptions."
        ],
        "answer": "The line graph shows how the output (on the y-axis) changes as you vary the input of interest (on the x-axis)."
    },
    {
        "question": "Change the value of the 'm' input from -0.05 to 0.1. What does the line graph look like now?",
        "options": [
            "A line sloping upwards going through $20,000,000 or so.",
            "A line sloping downwards going through $5,000,000 or so.",
            "An inverted U reaching its peak around $700,000 or so.",
            "A U-shape with its lowest point around $7,000,000 or so."
        ],
        "answer": "A line sloping upwards going through $20,000,000 or so."
    },
    {
        "question": "We use a data table in both sensitivity analysis and risk analysis. What’s the main difference?",
        "options": [
            "We systematically generate sequential input values for sensitivity analysis; we randomly generate input values in risk analysis.",
            "We always use different inputs for sensitivity analysis relative to risk analysis.",
            "The steps we follow to have Excel complete the data table using what-if analysis is fundamentally different.",
            "The data tables are generally much larger for sensitivity analysis."
        ],
        "answer": "We systematically generate sequential input values for sensitivity analysis; we randomly generate input values in risk analysis."
    },
    {
        "question": "Change the square foot input from 150,000 to 50,000. How does the histogram change?",
        "options": [
            "It gets more spread out and peaks around -1,000,000.",
            "It stays about the same spread and peaks around 0.",
            "It gets tighter and centers around approximately -3,000,000.",
            "It creates many peaks randomly located around various values.",
            "It does not change at all because the square foot input is unrelated."
        ],
        "answer": "It gets tighter and centers around approximately -3,000,000."
    },
    {
        "question": "Which best describes what this code does?\n\nunit_price_list = np.linspace(50,100,6)\nnet_earnings_outputs = [net_earnings(unit_price = i) for i in unit_price_list]",
        "options": [
            "It repeatedly executes the net_earnings model for unit_price input of 50, 60, 70, 80, 90, and 100, assuming the default values for the other inputs.",
            "It generates a list of unit_price values, but doesn't execute the net_earnings model.",
            "It applies the net_earnings model only to the first value in the unit_price_list and ignores the rest.",
            "It evaluates the average net earnings for unit_price values from 50 to 100, rounded to 6 decimal points.",
            "It makes a list of unit prices, then feeds it to a cat."
        ],
        "answer": "It repeatedly executes the net_earnings model for unit_price input of 50, 60, 70, 80, 90, and 100, assuming the default values for the other inputs."
    },
    {
        "question": "Which code would accomplish the task of calculating the percent likelihood that the net earnings will be over $480,000?\n\n\"Based on this assumed distribution of uncertainty of inputs, what is the percent likelihood that the net earnings will be over $480,000?\"",
        "options": [
            "np.mean(np.array(net_earnings_outputs) > 480000) which gives approximately 78%.",
            "np.sum(np.array(volume_random_inputs) > 480000) / 100 which gives approximately 73%.",
            "len(np.array(net_earnings_outputs) > 480000) which gives approximately 55%.",
            "np.median(net_earnings_outputs > 480000) which gives approximately 47%."
        ],
        "answer": "np.mean(np.array(net_earnings_outputs) > 480000) which gives approximately 78%."
    },
    {
        "question": "Consider the following statements. Which of them are true or false?\n\n1. It is often logical to present scenario analysis with a bar graph that compares the output values under each of the scenarios.\n2. Sensitivity analysis is typically shown using a line graph that illustrates how varying the value of an input larger or smaller affects the output.\n3. Risk analysis is typically shown with a stacked bar chart that shows the decomposition of risk for each scenario.",
        "options": [
            "1 and 2 are true; 3 is false.",
            "All are false.",
            "1 is false; 2 and 3 are true.",
            "All are true."
        ],
        "answer": "1 and 2 are true; 3 is false."
    },
    {
        "question": "Your boss wants to know how the sales price affects the breakeven point. What kind of analysis should you show him?",
        "options": [
            "Scenario analysis",
            "Sensitivity analysis",
            "Risk Analysis"
        ],
        "answer": "Sensitivity analysis"
    },
    {
        "question": "Your boss is considering selling independently or on a platform (e.g., Amazon). The two options have different fixed costs, variable costs, and sales prices. How do you help them decide which option to pursue?",
        "options": [
            "Scenario analysis",
            "Sensitivity analysis",
            "Risk Analysis"
        ],
        "answer": "Scenario analysis"
    },
    {
        "question": "Your boss says the variable cost is quite uncertain: their best guess is that it’s $25 per unit, but it could easily be anywhere between $15 and $35. How do you show how this uncertainty impacts the breakeven point?",
        "options": [
            "Risk Analysis",
            "Scenario analysis",
            "Sensitivity analysis"
        ],
        "answer": "Risk Analysis"
    },
    {
        "question": "Which statement about multivariate Monte Carlo analysis is correct?",
        "options": [
            "In multivariate Monte Carlo analysis, we generate random numbers directly for the output.",
            "In multivariate Monte Carlo analysis, we still focus on one input, but we generate many more outputs.",
            "In multivariate Monte Carlo analysis, we generate random numbers for more than one input to simulate each random output.",
            "In multivariate Monte Carlo analysis, we construct a multidimensional histogram in 3D for the output data."
        ],
        "answer": "In multivariate Monte Carlo analysis, we generate random numbers for more than one input to simulate each random output."
    },
    {
        "question": "How do you interpret the bar graph from at the end of the second video?",
        "options": [
            "The bars show the relative magnitudes of variation produced by the standard deviations assumed in the model.",
            "Negative bars mean the input is irrelevant to the model.",
            "Each bar shows the estimate from a linear regression of how much the output changes with one standard deviation change in the input.",
            "Each bar represents the total output produced by each input."
        ],
        "answer": "Each bar shows the estimate from a linear regression of how much the output changes with one standard deviation change in the input."
    }
]

def show_question(quiz_data, question_index):
    question = quiz_data[question_index]
    st.write(f"**Question {question_index + 1}**: {question['question']}")
    user_answer = st.radio("Choose your answer:", question["options"], key=f"radio_{question_index}")
    if st.button("Submit Answer", key=f"submit_{question_index}"):
        if user_answer == question["answer"]:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is: {question['answer']}")

# Streamlit app layout
st.title("Flashcard Quiz App")

# Navigation
question_index = st.number_input("Select question number:", min_value=1, max_value=len(quiz_data), step=1) - 1
show_question(quiz_data, question_index)


