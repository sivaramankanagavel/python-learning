import pickle

userDetails = {
    "name": "Sivaraman",
    "Age": 27,
    "profession": "Software"
}

# Writing to the pickle file
with open("pickle.txt", "wb") as pickleFile_write:
    pickle.dump(userDetails, pickleFile_write)

# Reading from the pickle file
with open("pickle.txt", "rb") as pickleFile_read:
    pickle_data = pickle.load(pickleFile_read)
    print(pickle_data)


