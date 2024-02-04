def main():
    text = input("enter your input: ")
    convert(text)

def convert(prompt):
    prompt = prompt.replace(':)','joy')
    prompt = prompt.replace(':(','sad')
    # return prompt
    print(prompt)

main()
