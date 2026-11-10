
import tiktoken

text = "i was taking a walk the other day ,and i see a women a blind women"

# encoding using encoding name
# encoding = tiktoken.get_encoding("cl100k_base")
# save_encoding_list = encoding.encode(text)

# print(save_encoding_list)
# print("Token count is :",len(save_encoding_list))

# using encoding model --- gpt-40-mini
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
save_encoding_list = encoding.encode(text)
print(save_encoding_list)
print("Token count is :",len(save_encoding_list))


# using encoding model
# encoding = tiktoken.get_encoding("r50k_base")
# save_encoding_list = encoding.encode(text)
# print(save_encoding_list)
# print("Token count is :",len(save_encoding_list))

# trying to know model gpt-6 uses which encoding
encoding = tiktoken.encoding_for_model("gpt-5")
save_encoding_list = encoding.encode(text)
print(save_encoding_list)
print("Token count is :",len(save_encoding_list))




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

for model in ["gpt-5", "gpt-4o-mini"]:
    encoding = tiktoken.encoding_for_model(model)
    print(model, "->", encoding.name)