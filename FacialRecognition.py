import os

"""calls an OpenFace scrypt called classifier to facial recognaize an image.
    Returns:
        return 0 if user is not recognize, or there is no photo in folder
        return 1 if user is identified with "+80%" accuracy.
"""
def facialRecognition():
    path1 = "/Applications/ShreddedEncryption/appImages/pic.jpg"
    path2 = "/Users/fedo/Desktop/LastTry/openface/"
    if os.path.exists(path1):
        person = []
        confidence = []
        open(path2 + "personinfo", 'w').write("")
        open(path2 + "confidenceinfo", 'w').write("")
        os.system('cd ' + path2 + 'torch/ && source install/bin/torch-activate && cd .. && ./demos/classifier.py infer ./data/idata/rep/classifier.pkl ' + path1)
        os.remove(path1)
        with open(path2 + "personinfo", 'r') as f:
            for line in f:
                person.append(line.replace("\n", ""))
        f.close()
        with open(path2 + "confidenceinfo", 'r') as f:
            for line in f:
                confidence.append(line.replace("\n", ""))
        f.close()
        if len(person) > 0 and len(confidence) > 0:
            if person[0] == 'FahadAlhajjaj' and float(confidence[0]) >= 0.80:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0