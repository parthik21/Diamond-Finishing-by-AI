from PIL import Image

def train_img_rotation():
    
    for i in range(1,11):
        image = Image.open("../Project DF-AI/DataSet/Resized/image"+str(i)+".jpg");

        for j in range(90):
            rotated_img = image.rotate(j*4)
            rotated_img.save("../Project DF-AI/DataSet/Train_DataSet/image"+str(i)+"_"+str(j)+".jpg");
            
def test_img_rotation():
    
    for i in range(11,14):
        image = Image.open("../Project DF-AI/DataSet/Resized/image"+str(i)+".jpg");
        
        for j in range(90):
            rotated_img = image.rotate(j*4)
            rotated_img.save("../Project DF-AI/DataSet/Test_DataSet/image"+str(i)+"_"+str(j)+".jpg");
