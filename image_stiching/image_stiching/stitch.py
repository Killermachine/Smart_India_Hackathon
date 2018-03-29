import cv2
import numpy as np
import os

class ImageStitch:
	def __init__(self,directory):
		self.img1 = None
		self.img2 = None
		self.stitched_image = None
		self.img1_points = []
		self.img2_points = []
		self.directory = directory
	
	def get_img1(self,path):
		self.img1 = cv2.imread(path)
		#cv2.imshow("img",self.img1)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

	def get_img2(self,path):
		self.img2 = cv2.imread(path)

	def _show_images(self):
		img = np.hstack((self.img1, self.img2))
		cv2.imshow("img",img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
	def _key_points_matcher(self):
		sift = cv2.xfeatures2d.SIFT_create()
		
		key1, desc1 = sift.detectAndCompute(self.img1, None)
		key2, desc2 = sift.detectAndCompute(self.img2, None)

		brute_force_matcher = cv2.BFMatcher()
		matches = brute_force_matcher.knnMatch(desc1, desc2, k=2)

		for match in matches:
			self.img1_points.append(key1[match[0].queryIdx].pt)
			self.img2_points.append(key2[match[0].trainIdx].pt)
		
		self.img1_points = np.float32(self.img1_points).reshape(-1,1,2)
		self.img2_points = np.float32(self.img2_points).reshape(-1,1,2)

		M, mask = cv2.findHomography(self.img1_points, self.img2_points, cv2.RANSAC, 5.0)
		self.img1_points = []
		self.img2_points = []
		return M
	
	def _stitch_images(self, M):
		w1,h1 = self.img2.shape[:2]
		w2,h2 = self.img1.shape[:2]

		img1_dims = np.float32([ [0,0], [0,w1], [h1, w1], [h1,0] ]).reshape(-1,1,2)
		img2_dims_temp = np.float32([ [0,0], [0,w2], [h2, w2], [h2,0] ]).reshape(-1,1,2)

		img2_dims = cv2.perspectiveTransform(img2_dims_temp, M)

		result_dims = np.concatenate( (img1_dims, img2_dims), axis = 0)

		[x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
		[x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
		
		transform_dist = [-x_min,-y_min]
		transform_array = np.array([[1, 0, transform_dist[0]], 
									[0, 1, transform_dist[1]], 
									[0,0,1]]) 

		result_img = cv2.warpPerspective(self.img1, transform_array.dot(M), 
										(x_max-x_min, y_max-y_min))
		result_img[transform_dist[1]:w1+transform_dist[1],transform_dist[0]:h1+transform_dist[0]] = self.img2

		self.stitched_image = result_img

	def main(self):
		self.get_img1(self.directory + "/1.png")
		self.get_img2(self.directory + "/2.png")
		M = self._key_points_matcher()
		self._stitch_images(M)
		#cv2.imshow("image_stitched",self.stitched_image)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		cv2.imwrite(self.directory +'/stitched_image.png',self.stitched_image)
		image_list = [self.directory + "/" + image for image in os.listdir(self.directory)]
		for i in range(3,len(image_list)):
			print i
			self.get_img1(self.directory + "/stitched_image.png")
			self.get_img2(self.directory + "/" + str(i) +".png")
			M = self._key_points_matcher()
			self._stitch_images(M)
			cv2.imshow("image_stitched",self.stitched_image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			cv2.imwrite(self.directory +'/stitched_image.png',self.stitched_image)	        

		#print(self.img1.shape)
		#self._show_images()
		#M = self._key_points_matcher()
		#self._stitch_images(M)
		cv2.imshow("image_stitched",self.stitched_image)
		cv2.waitKey()
		cv2.destroyAllWindows()
stitch = ImageStitch("./ahmedabad")
stitch.main()