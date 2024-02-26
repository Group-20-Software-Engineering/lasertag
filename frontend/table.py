

def table():
    for row in range(16):
            RowRedRect = []

            for col in range(2):
                x = col * rectWidth
                y = row * rectHeight + 44
                rect = pygame.Rect(x, y, rectWidth, rectHeight)
                pygame.draw.rect(screen, BLACK, rect, 1)
                pygame.draw.rect(screen, RED, rect.inflate(-2, -2))
                RowRedRect.append(rect)
                if row == 0 and col == 0:
                    textWords = "ID"
                if row == 0 and col == 1:
                    textWords = "CodeName"
                if row == 1 and col == 0:
                    red_Id.append(userInput)
                    print(red_Id[1])
                    textWords = red_Id[0]
                if row == 1 and col == 1:
                    textWords = "name"
                text = coolFont.render(textWords, True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                # Blit text onto the screen
                screen.blit(text, text_rect)
            RedTable.append(RowRedRect)