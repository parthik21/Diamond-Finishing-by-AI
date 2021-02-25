#Prepare Images to use as a DataBase
ri.test_img_rotation();
ri.train_img_roration();


#Extract images pixel values from created data
test_images = ei.extract_test_images();
train_images = ei.extract_train_images();

#Create lables
test_lables = chdf.create_test_lables();
train_lables = chdf.create_train_lables();

#Store data in HDF
chdf.store_test_data(test_images, test_labels);
chdf.store_test_data(train_images, train_labels);
