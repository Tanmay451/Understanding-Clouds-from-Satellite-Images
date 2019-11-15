import csv
import os
import cv2
loc = 'C:/Users/tanma/OneDrive/Desktop/Naruto/understanding_cloud_organization/train_xl'
x_train = []
y_train = []
rows = []
name = []
for xl in os.listdir(loc):
    with open(os.path.join(loc, xl), 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
#print(rows[0])
for i in range(1, len(rows)):
    y_train.append(rows[i][0])
    x_train.append(rows[i][1])
#print(y_train)
for i in range(len(y_train)):
    a = y_train[i].split('_')
    y_train[i] = a[1]
    name.append(a[0])
for i in range(len(x_train)):
    x_train[i] = x_train[i].split()
    if(x_train[i]):
        a = int(x_train[i][0])
        #b = int(x_train[i][1])
        #b = a + b
        c = int(x_train[i][-2])
        d = int(x_train[i][-1])
        #d = c + d
        x_train[i] = [a,c,d]
path = 'C:/Users/tanma/OneDrive/Desktop/Naruto/understanding_cloud_organization/train_images'
img_path = 'C:/Users/tanma/OneDrive/Desktop/Naruto/understanding_cloud_organization/train_images2'
#print(x_train[0][0])
for i in range(len(x_train)):
    if(x_train[i]):
        img = cv2.imread(os.path.join(path, name[i]))
        x1 = int(x_train[i][0] / 1400)
        y1 = int(x_train[i][0] % 1400)
        x2 = int(x_train[i][1] / 1400)
        y2 = int((x_train[i][1] % 1400)+(x_train[i][2]))
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = name[i].split('.')
        b[0] = b[0] + '_' + str(i)
        a = '.'
        a = a.join(b)
        print(a)
        cv2.putText(img, y_train[i], (10,450), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite(os.path.join(img_path, a), img)
        print(i, 'Successful')
#x_train.append(rows[1])
#x_train[0].pop(0)
#x_t = [int(i) for i in x_train[0][0].split()]

#img = cv2.rectangle(img, (318, 189), (1255, 1183), (255, 0, 0), 5)
#cv2.imshow('Image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
