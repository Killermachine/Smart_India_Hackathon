import cv2
import numpy as np

class GenGrid:
	def __init__(self,width,height):
		self.map_width = width
		self.map_height = height
		self.width_ratio = 0.0
		self.height_ratio = 0.0
		self.map_image = None
		self.lat_long_mat = None
		self.grid_width = None
		self.grid_height = None

	def _set_map_image(self,path):
		self.map_image = cv2.imread(path)

	def _show_map(self):
		cv2.imshow("map",self.map_image)
		cv2.waitKey()
		cv2.destroyAllWindows()

	def _draw_rect_on_map(self,x,y,w,h,color,alpha):
		overlay = self.map_image.copy()
		output = self.map_image.copy()
		cv2.rectangle(overlay, (int(x*self.width_ratio),int(y*self.height_ratio)), (int((x+w)*self.width_ratio),int((y+h)*self.height_ratio)),color,-1)
		cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)
		self.map_image = output
	
	def _render_grid(self,path,grid_list,w,h):
		self._set_map_image(path)
		(height,width,channel) = self.map_image.shape
		self.width_ratio = width/float(self.map_width)
		self.height_ratio = height/float(self.map_height)
		for x,y,color,factor_of_completion in grid_list:
			self._draw_rect_on_map(x,y,w,h,color,factor_of_completion)
		self._show_map()

	def _render_points(self,path,point_list):
		"""
		point_list is List of list, containg x,y, color where color is in the form (0,0,0)
		"""
		if self.map_image is None:
			self._set_map_image(path)
			(height,width,channel) = self.map_image.shape
			self.width_ratio = width/float(self.map_width)
			self.height_ratio = height/float(self.map_height)
		for point_x,point_y,color in point_list:
			cv2.circle(self.map_image,(int(point_x*self.width_ratio),int(point_y*self.height_ratio)),3,color,3)
		self._show_map()
	
# x,y in the real dimentions
grid = GenGrid(1000,1000)
# x,y, <color_as_tuple>, <factor of ompletion>
# factor of completion 85% = 0.85
point_list = [[500,500,(0,0,255)],[400,500,(0,255,255)]]
grid_list = [[0,0,(0,0,255),0.5],[100,100,(0,255,0),0.9]]

 for point in point_list:
	#grid.render_grid("./img.png",grid_list,100,100)
	grid._render_points("./img.png",[point])
	
