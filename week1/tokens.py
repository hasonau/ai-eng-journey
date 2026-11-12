
import tiktoken

text = "i was taking a walk the other day ,and i see a women a blind women"
english_text = "Artificial intelligence is transforming software engineering."

code_text = """def calculate_total(price, quantity):
    return price * quantity"""

numbers_text = "1250.75 42 2026 123456789 3.1415926535"

# encoding using encoding name
# encoding = tiktoken.get_encoding("cl100k_base")
# save_encoding_list = encoding.encode(text)

# print(save_encoding_list)
# print("Token count is :",len(save_encoding_list))

# using encoding model --- gpt-40-mini
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
save_encoding_list1 = encoding.encode(english_text)
save_encoding_list2 = encoding.encode(code_text)
save_encoding_list3 = encoding.encode(numbers_text)

print(save_encoding_list1)
print("Token count is :",len(save_encoding_list1))
print(save_encoding_list2)
print("Token count is :",len(save_encoding_list2))
print(save_encoding_list3)
print("Token count is :",len(save_encoding_list3))


texts = {
    "English": english_text,
    "Code": code_text,
    "Numbers": numbers_text
}

for name, content in texts.items():
    tokens = len(encoding.encode(content))
    characters = len(content)

    print(f"{name}: {tokens} tokens / {characters} characters")
    print("Ratio:", round(tokens / characters, 3))


# using encoding model
# encoding = tiktoken.get_encoding("r50k_base")
# save_encoding_list = encoding.encode(text)
# print(save_encoding_list)
# print("Token count is :",len(save_encoding_list))

# trying to know model gpt-6 uses which encoding
# encoding = tiktoken.encoding_for_model("gpt-5")
# save_encoding_list = encoding.encode(text)
# print(save_encoding_list)
# print("Token count is :",len(save_encoding_list))




# def compare_encodings(example_string: str) -> None:
#     """Prints a comparison of three string encodings."""
#     # print the example string
#     print(f'\nExample string: "{example_string}"')
#     # for each encoding, print the # of tokens, the token integers, and the token bytes
#     for encoding_name in ["r50k_base", "p50k_base", "cl100k_base", "o200k_base"]:
#         encoding = tiktoken.get_encoding(encoding_name)
#         token_integers = encoding.encode(example_string)
#         num_tokens = len(token_integers)
#         token_bytes = [encoding.decode_single_token_bytes(token) for token in token_integers]
#         print()
#         print(f"{encoding_name}: {num_tokens} tokens")
#         print(f"token integers: {token_integers}")
#         print(f"token bytes: {token_bytes}")

# compare_encodings("somethingisgoingtohappen")

# for model in ["gpt-5", "gpt-4o-mini"]:
#     encoding = tiktoken.encoding_for_model(model)
#     print(model, "->", encoding.name)