filenames=["1.old","2.new","3.some"]
for filename in filenames:
    filename=filename.replace('.','|',1)
    print(filename)