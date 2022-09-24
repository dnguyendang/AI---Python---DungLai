import pygame
from random import randint
import math

# thu vien danh rieng cho phan algorithm 
from sklearn.cluster import KMeans
#tao ham viet text, thay vi nhap nhieu dong giong nhau 
# def create_text_render(string):
# 	font = pygame.font.SysFont('sans', 40)
# 	return font.render(string, True, WHITE)

def distance(p1, p2):
	return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

# initialize
#khoi tao nhung thu pygame co the dung duoc 
pygame.init() 

#tao ra man hinh 
screen = pygame.display.set_mode((1200,700))

#tao ten cho chuong trinh hien thi
pygame.display.set_caption("kmeans visualization")


running = True

#tao khung hinh xuat hien tren giay, fps 
clock = pygame.time.Clock()

#chon mau cho background theo ma mau Red, Green, Blue 
BACKGROUND = (214,214,214)
BLACK = (0,0,0)
YELLOW = (249,255,230)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (255,0,255)
GRESS = (55,155,65)
GRAPE = (100,25,125)
ORANGE = (255,125, 25)

COLORS = [RED, GREEN, BLACK, PURPLE, GRESS, GRAPE, ORANGE]

#tao font chu 
font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
#tao text 
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render('run', True, WHITE)
text_random = font.render('random', True, WHITE)
text_algorithm = font.render('algorithm', True, WHITE)
text_reset = font.render('reset', True, WHITE)

K = 0
error = 0
points = []
clusters = []
# label la nhan cua cac point, mau cua cac diem point 
labels = []

#end initialize

#draw on the screen

#cho hinh anh chay lien tuc de tao ra chuong trinh 
while running:
	clock.tick(60)
	screen.fill(BACKGROUND)
	#lay toa do chuot
	mouse_x, mouse_y = pygame.mouse.get_pos()

	#draw interface
	#draw panel 
	pygame.draw.rect(screen, BLACK, (50,50,700,500))
	pygame.draw.rect(screen,YELLOW, (55,55,690,490))

	#K button +
	pygame.draw.rect(screen, BLACK, (850,50,50,50))
	#toa do text
	screen.blit(text_plus,(865,50))

	#	K button -
	pygame.draw.rect(screen, BLACK,(950,50,50,50))
	screen.blit(text_minus,(970,50))

	# K value 
	text_k = font.render("K = " + str(K), True, BLACK)
	screen.blit(text_k, (1050,50))

	#	run button
	pygame.draw.rect(screen, BLACK, (850,150,150,50))
	screen.blit(text_run, (900, 150))

	#random button 
	pygame.draw. rect (screen, BLACK, (850,250,150,50))
	screen.blit(text_random, (850,250))

	#algorithm button scikit-learn
	pygame.draw.rect(screen, BLACK, (850, 450, 150,50))
	screen.blit(text_algorithm, (850,450))

	#reset button 
	pygame.draw.rect(screen,BLACK, (850,550,150,50))
	screen.blit(text_reset, (850,550))

	#error text
	text_error = font.render("Error = " + str(int(error)), True, BLACK)
	screen.blit(text_error, (850, 350))

	# draw mouse position when mouse is in panel
	if 50 < mouse_x < 750 and 50 < mouse_y< 550:
		text_mouse = font_small.render("(" + str(mouse_x-50) + "," + str(mouse_y-50) + ")", True, BLACK)
		screen.blit(text_mouse, (mouse_x +5, mouse_y-20))

	#end draw interface

	#lay toa do chuot
	mouse_x, mouse_y = pygame.mouse.get_pos()

	#tao nhung su kien (an nut, an chuot) 
	for event in pygame.event.get():
		#tao nut tat
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			#create point on panel 
			if 50 < mouse_x < 750 and 50 < mouse_y < 550:
				labels = []
				point = [mouse_x , mouse_y]
				points.append(point)
				print (points)

			#change K button +
			if 850 < mouse_x <900 and 50 < mouse_y < 100:
			# toa do x va y cua khung hinh +  	
				if K < 6 :
				# vi chi co 7 mau 
					K += 1
				print ("press k +")

			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
				if K > 0:
					K -= 1
				print ("press k -")

			# run button 
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200: 
				# khi khong can thay doi gia tri thi tao 1 copy, chung ta se dung for p in points 
				labels = []

				#sua loi nut run khi chua co du lieu 
				if clusters == []:
					continue
				# assign points to closet clusters
				for p in points:
				# for i in range(len(points)): , khi can thay doi gia tri 
				# i la tung diem point trong points, truc tiep lay gia tri trong point 
					distances_to_cluster = []
					for c in clusters:
						dis = distance (p , c)
						distances_to_cluster.append(dis)

					min_distance = min(distances_to_cluster)
					label = distances_to_cluster.index(min_distance)
					labels.append(label)

				# update clusters 
				for i in range(K):
					sum_x = 0 
					sum_y = 0
					count = 0
					for j in range(len(points)):
						if labels[j] == i:
						# tuc la nhan cua point do trung vs mau cua cluster K 
							sum_x += points[j][0]
							sum_y += points[j][1]
							count += 1
					if count != 0:
						new_cluster_x = sum_x / count
						new_cluster_y = sum_y / count
						clusters[i] = [new_cluster_x, new_cluster_y]

				print("run pressed")

			#random button 
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
				labels = []
				clusters = []
				for i in range(K):
					random_point = [randint(50,750), randint(50,550)] 
					#panel co chieu ngang 700 chieu doc 500
					clusters.append(random_point)
				print ("random pressed")

			#reset button 
			if 850 < mouse_x < 1000 and 550 < mouse_y <600:
				K = 0
				error = 0
				points = []
				clusters = []
				labels = []
				print ("reset pressed")

			#algorithm button 
			if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
				# if K == 0:
				# 	continue
				#co the dung if hoac dung ham try - except de bat loi 
				try:
					kmeans = KMeans(n_clusters=K).fit(points)
					#KMeans la ten ham 
					#n_clusters la 1 cai parameter 
					# fit -> dang train model -> toi uu model, fit vs data -> dang huan luyen no de lam vc vs du lieu 

					print(kmeans.cluster_centers_) 
					# day la vi tri cua clusters sau cung 

					labels = kmeans.predict(points)
					#du doan du lieu theo index hay label

					clusters = kmeans.cluster_centers_
					#gan luon 
				except: 
					print("runtime_error")
					continue
				# dung thu vien khong phai la code yeu
					#quan trong
					## o ki nang thay doi parameter dua vao
					##xay dung he thong xung quanh no (software engineer)
					## xu ly du lieu vao tot
					## biet cach can dong do dem xem thuat toan nao la toi uu la tot hon 
				#trong ML luon co cac ham fit: training va predict: du doan 
				# kmean ++ thuat toan de chon random sao cho toi uu 
				# trong chuong trinh can dung nhieu try-except de chuong trinh ko de bi do vo 
				print ("algorithm pressed") 

	#draw cluster
	for i in range(len(clusters)):
		pygame.draw.circle(screen,COLORS[i],(int(clusters[i][0]),int(clusters[i][1])), 10)
 
	#draw point 
	for i in range(len(points)):
		pygame.draw.circle(screen,BLACK, (points[i][0] , points[i][1] ), 6)
		if labels == []:
			pygame.draw.circle(screen,WHITE, (points[i][0] , points[i][1] ), 5)		
		else:
			pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0], points[i][1]), 5)

	#calculate and draw error 
	error = 0
	if clusters != [] and labels != []:
		for i in range(len(points)):
			error += distance(points[i], clusters[labels[i]])
	text_error = font.render("Error = " + str(int(error)), True, BLACK)
	screen.blit(text_error, (850, 350))
	#lenh de tao hieu luc cho cac dung lenh phia tren trong lap trinh do hoa 
	pygame.display.flip()

# end draw 

#xoa du lieu do ton bo nho
pygame.quit() 

# loi xay ra khi chay -> quay ve xem trong phan #run , loi nay goi la runtime_error 