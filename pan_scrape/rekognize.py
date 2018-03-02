import boto3
import os


rekog = boto3.client("rekognition")

def identify(filename):
    img = open(filename, "rb")
    data = img.read()
    my_dict = dict()
    my_dict["Bytes"] = data
    r = rekog.detect_text(Image = my_dict)
    ans = r["TextDetections"][0]["DetectedText"]
    lol = clean_rekog(ans)
    return lol


def clean_rekog(ans):
    for char in ans:
        if char.islower():
            ans = ans.replace(char, char.upper())
            print(ans)
        if not char.isalnum():
            print(ans)
            ans = ans.replace(char, "")
            print(ans)
    if len(ans)>5:
        if "II" in ans:
            ans = ans.replace("II", "H")
    return ans

# print(identify("readable_captchas/"))


# for filename in os.listdir("readable_captchas"):
#     img = cv.imread("readable_captchas/" + filename)
#     # window = cv.namedWindow("lol")
#     # cv.imshow(window, img)
#     s = pts.image_to_string(img, config="-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -psm 6")
#     print(filename, s)