import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def __generate_gpt3_response(prompt: str):
    if len(prompt) < 30:
        return ""
    completions = openai.Completion.create(
        engine='text-davinci-003',
        temperature=0.5,
        prompt=prompt,
        max_tokens=2500,
        n=1,
        stop=None,
    )
    return completions.choices[0].text


def solve_leetcode(problem: str, language: str = "Python"):
    prompt = f"""Solve the following programming problem in {language}:\n\n{problem}\n\nAnswer in {language}:\n"""
    return __generate_gpt3_response(prompt)


def solve_api_design(problem: str):
    prompt = f"""You are to design an API schema:\n\n{problem}\n\nAnswer:\n"""
    return __generate_gpt3_response(prompt)
