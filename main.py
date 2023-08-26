import hashlib
pass_count=0
word_hash = input("Enter Password in hashed format ")
p_doc = input("\n Enter wordlist including path")
p_file = open(p_doc, 'r')
for word in p_file:
    enc_word=word.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()
    if digest == word_hash:
     print("Password found: ", word)
    pass_count=1
    break
if  not pass_count:
    print("password not found")