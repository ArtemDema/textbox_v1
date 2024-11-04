import pygame
screen = pygame.display.set_mode((1000, 600))
pygame.init()


class TextBox():    #Класс текстбокса
    def __init__(self, x, y, widht, height, print_text, input_text, size_text):
        self.x_left = x                             #Положение по x
        self.y_top = y                              #Положение по y
        self.width = widht                          #Ширина
        self.height = height                        #Высота
        self.print_text = print_text                #Пытается ли пользователь ввести текст в этот текстбар
        self.input_text = input_text                #Что сейчас написано в текстбоксе
        self.size_text = size_text                  #
        self.x_right = self.x_left + self.width     #Нужно для понимания, нажали ли на область текстбара
        self.y_bottom = self.y_top + self.height    #Нужно для понимания, нажали ли на область текстбара
        self.f = pygame.font.Font(None, self.size_text)

    def click_on_textbar(self, mouse_x, mouse_y): #Проверка на нажатие на область текстбара
        if mouse_x >= self.x_left:
            if mouse_x <= self.x_right:
                if mouse_y >= self.y_top:
                    if mouse_y <= self.y_bottom:
                        return True     #Если нажали, то говорим что надо выводить всё что будет писать пользователь
        return False
    
    def print_in_text(self):    #Проверка, на то, пытается ли пользователь что то ввести в какой то текстбар
        if self.print_text:                                     #Проверка если что то да пытается ввести
            if event.key == pygame.K_RETURN:                    #Если нажал Enter
                self.print_text = False
            if event.key == pygame.K_BACKSPACE:                 #Если нажал BackSpace
                self.input_text = self.input_text[:-1]          #Убираем последнюю букву через обрезание ))))
            else:
                self.input_text += event.unicode                #Добавляем введённую букву к тексту
    
    def print_text_on_screen(self):
        text = self.f.render(self.input_text, True, (255, 255, 255)) #текст, сглаживание, цвет
        screen.blit(text, (self.x_left, self.y_top))



list_textboxes = []     #Список текстбоксов

text_box1 = TextBox(0, 0, 100, 100, False, "qwerty", 36)  #Сам текстбокс
text_box2 = TextBox(0, 500, 100, 100, False, "qwerty", 36)  #Сам текстбокс

list_textboxes.append(text_box1)    #Добавляенм текстбокс1 к собратьям
list_textboxes.append(text_box2)

game_run = True
while game_run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

        if event.type == pygame.MOUSEMOTION: 
            position_mouse = event.pos  #Запоминаем позицию мыши

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #если нажали ЛКМ
            for text_box in list_textboxes:
                text_box.print_text = text_box.click_on_textbar(position_mouse[0], position_mouse[1])   #Посылаем проверять

        if event.type == pygame.KEYDOWN:
            for text_box in list_textboxes:
                text_box.print_in_text()      #Посылаем проверять на печать текста пользователем

    for text_box in list_textboxes: #Вывод текста
        text_box.print_text_on_screen()

    pygame.display.flip()