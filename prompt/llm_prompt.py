agent_roles_datasets = {
    "finance": {
        "expert": "An expert skilled in analyzing corporate financial risks based on corporate economic indicators and fundamental characteristics."
    },
    "ceo": {
        "expert": "An expert skilled in grading corporate management levels based on corporate executive member information."
    },
    "news": {
        "expert": "An expert skilled in scoring the intensity of negative corporate public sentiment based on negative corporate news."
    },
    "laws": {
        "expert": "An expert skilled in scoring corporate litigation risks based on corporate legal litigation events."
    },
    "vios": {
        "expert": "An expert skilled in scoring corporate violation risks based on corporate violation events."
    },
}

agent_characters = {
    "temperate": "Objective and fair; you will be persuaded if other agents' answers make sense.",
    "confident": "Confident in your own answers and frequently persuade other agents to believe you."
}

interaction_prompt = {
    "finance": {
        "question": "Suppose the latest data of a listed company for a certain year is \"{}\", the annual industry analysis report for that year is \"{}\", and the annual stock K-line chart analysis report is \"{}\". Please score the company's financial risk for that year from 0 to 100, where 0-20: extremely low risk, 21-40: low risk, 41-60: medium risk, 61-80: high risk, 81-100: extremely high risk, with 100 representing the highest risk. Pay special attention to the retained earnings to total assets ratio and the cost-expense profit margin. Please explain your answer and provide your final score rounded to one decimal place on a new line at the very end. The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
        "debate": [
            "Here are the financial risk ratings from other analysts:",
            "\n\nCan you carefully check if your rating is accurate? Please review the reasoning of other analysts and your historical ratings. Divide your final answer into a score of 0-100, where 0-20: extremely low risk, 21-40: low risk, 41-60: medium risk, 61-80: high risk, 81-100: extremely high risk, with 100 representing the highest risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
        ],
        "reflection": "Can you carefully check if your rating is accurate? Review the reasoning behind your historical ratings. Give your final answer as a score from 0-100, where 0-20: extremely low risk, 21-40: low risk, 41-60: medium risk, 61-80: high risk, 81-100: extremely high risk, with 100 representing the highest risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
    },
    "ceo": {
        "question": "Suppose the executive member information of a listed company for a certain year is \"{}\", and the company's negative news for that year is as follows: \"{}\". Please score the company's management level for that year based on this information, ranging from 0 to 100, where 0-20: extremely weak management quality, 21-40: weak management quality, 41-60: medium management quality, 61-80: strong management quality, 81-100: extremely strong management quality, with 100 representing the highest management quality. Please explain your answer and provide your final score as a numerical value rounded to one decimal place on the last line. The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
        "debate": [
            "Here are the management level ratings from other analysts:",
            "\n\nCan you carefully check if your rating is accurate? Please review the reasoning of other analysts and your historical ratings. Divide your final answer into a score of 0-100, where 0-20: extremely weak management quality, 21-40: weak management quality, 41-60: medium management quality, 61-80: strong management quality, 81-100: extremely strong management quality, with 100 representing the highest management quality. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
        ],
        "reflection": "Can you carefully check if your rating is accurate? Review the reasoning behind your historical ratings. Give your final answer as a score from 0-100, where 0-20: extremely weak management quality, 21-40: weak management quality, 41-60: medium management quality, 61-80: strong management quality, 81-100: extremely strong management quality, with 100 representing the highest management quality. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
    },
    "news": {
        "question": "Given a listed company with basic information \"{}\", the company's annual negative news content is \"{}\". Please score the intensity of the company's negative public sentiment from 0 to 100, where 0: no negative sentiment, 1-20: extremely low negative sentiment intensity, 21-40: low negative sentiment intensity, 41-60: medium negative sentiment intensity, 61-80: high negative sentiment intensity, 81-99: extremely high negative sentiment intensity, with 100 representing the highest negative sentiment intensity. Please explain your answer and provide your final score rounded to one decimal place on a new line at the very end. The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
        "debate": [
            "Here are the negative public sentiment intensity ratings from other analysts:",
            "\n\nCan you carefully check if your rating is accurate? Please review the reasoning of other analysts and your historical ratings. Divide your final answer into a score of 0-100, where 0: no negative sentiment, 1-20: extremely low negative sentiment intensity, 21-40: low negative sentiment intensity, 41-60: medium negative sentiment intensity, 61-80: high negative sentiment intensity, 81-99: extremely high negative sentiment intensity, with 100 representing the highest negative sentiment intensity. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
        ],
        "reflection": "Can you carefully check if your rating is accurate? Review the reasoning behind your historical ratings. Give your final answer as a score from 0-100, where 0: no negative sentiment, 1-20: extremely low negative sentiment intensity, 21-40: low negative sentiment intensity, 41-60: medium negative sentiment intensity, 61-80: high negative sentiment intensity, 81-99: extremely high negative sentiment intensity, with 100 representing the highest negative sentiment intensity. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
    },
    "laws": {
        "question": "Given a listed company with basic information \"{}\", the company's annual legal litigation content is \"{}\". Please score the company's litigation risk from 0 to 100, where 0: no litigation risk, 1-20: extremely low litigation risk, 21-40: low litigation risk, 41-60: medium litigation risk, 61-80: high litigation risk, 81-99: extremely high litigation risk, with 100 representing the highest litigation risk. Please explain your answer and provide your final score rounded to one decimal place on a new line at the very end. The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
        "debate": [
            "Here are the litigation risk ratings from other analysts:",
            "\n\nCan you carefully check if your rating is accurate? Please review the reasoning of other analysts and your historical ratings. Divide your final answer into a score of 0-100, where 0: no litigation risk, 1-20: extremely low litigation risk, 21-40: low litigation risk, 41-60: medium litigation risk, 61-80: high litigation risk, 81-99: extremely high litigation risk, with 100 representing the highest litigation risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
        ],
        "reflection": "Can you carefully check if your rating is accurate? Review the reasoning behind your historical ratings. Give your final answer as a score from 0-100, where 0: no litigation risk, 1-20: extremely low litigation risk, 21-40: low litigation risk, 41-60: medium litigation risk, 61-80: high litigation risk, 81-99: extremely high litigation risk, with 100 representing the highest litigation risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
    },
    "vios": {
        "question": "Given a listed company with basic information \"{}\", the company's annual violation event content is \"{}\". Please score the company's violation risk from 0 to 100, where 0: no violation risk, 1-20: extremely low violation risk, 21-40: low violation risk, 41-60: medium violation risk, 61-80: high violation risk, 81-99: extremely high violation risk, with 100 representing the highest violation risk. Please explain your answer and provide your final score rounded to one decimal place on a new line at the very end. The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics.",
        "debate": [
            "Here are the violation risk ratings from other analysts:",
            "\n\nCan you carefully check if your rating is accurate? Please review the reasoning of other analysts and your historical ratings. Divide your final answer into a score of 0-100, where 0: no violation risk, 1-20: extremely low violation risk, 21-40: low violation risk, 41-60: medium violation risk, 61-80: high violation risk, 81-99: extremely high violation risk, with 100 representing the highest violation risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
        ],
        "reflection": "Can you carefully check if your rating is accurate? Review the reasoning behind your historical ratings. Give your final answer as a score from 0-100, where 0: no violation risk, 1-20: extremely low violation risk, 21-40: low violation risk, 41-60: medium violation risk, 61-80: high violation risk, 81-99: extremely high violation risk, with 100 representing the highest violation risk. Round to one decimal place on the last line of your response! The final score must be presented in the format of 'Final Score:'. The analysis process should be concise, highlighting the key points for each dimension's characteristics."
    }
}