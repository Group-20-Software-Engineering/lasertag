import pygame

RedTable = []
GreenTable = []
rectWidth = 900/4
rectHeight = 580/16
textWords = ''

def drawRect(row, col, x, y, rectWidth, rectHeight, screen, borderColor, fillColor) -> pygame.Rect:
    rect = pygame.Rect(x, y, rectWidth, rectHeight)
    pygame.draw.rect(screen, borderColor, rect, 1)
    pygame.draw.rect(screen, fillColor, rect.inflate(-2, -2))
    return rect

def drawLeftTable(RedTable, listNotEmpty, RedTeam, coolFont, screen, borderColor, fillColor, fontColor, textWords):
    for row in range(15):
                    RowRedRect = []

                    for col in range(2):
                        x = col * rectWidth #determine x coordinate for each rectangle
                        y = row * rectHeight + 44 #determine y coordinate for each rectangle
                        rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, borderColor, fillColor) #draw red rectangle
                        RowRedRect.append(rect)
                        if (len(RedTeam.redPlayers) == 0):
                            pass
                        elif (listNotEmpty == True):
                            if col == 0 and row < len(RedTeam.redPlayers):
                                textWords = RedTeam.redPlayers[row].id
                            if col == 1 and row < len(RedTeam.redPlayers):
                                textWords = RedTeam.redPlayers[row].codename
                            if row >= len(RedTeam.redPlayers):
                                textWords = " "
                        text = coolFont.render(textWords, True, fontColor)
                        text_rect = text.get_rect(center=rect.center)
                        # Blit text onto the screen
                        screen.blit(text, text_rect)
                        
                    RedTable.append(RowRedRect)

def drawRightTable(RightTable, listNotEmpty, GreenTeam, coolFont, screen, borderColor, fillColor, fontColor, textWords):
     for row in range(15):
                RowGreenRect = []
                for col in range(2):
                    x = col * rectWidth + screen.get_width() / 2 #determine x coordinate for each rectangle
                    y = row * rectHeight + 44 #determine y coordinate for each rectangle
                    rect = drawRect(row, col, x, y, rectWidth, rectHeight, screen, borderColor, fillColor) #draw green rectangle
                    if (len(GreenTeam.greenPlayers) == 0):
                        pass
                    elif (listNotEmpty == True):
                        if col == 0 and row < len(GreenTeam.greenPlayers):
                            textWords = GreenTeam.greenPlayers[row].id
                        if col == 1 and row < len(GreenTeam.greenPlayers):
                            textWords = GreenTeam.greenPlayers[row].codename
                        if row >= len(GreenTeam.greenPlayers):
                            textWords = " "
                    text = coolFont.render(textWords, True, fontColor)
                    text_rect = text.get_rect(center=rect.center)
                    # Blit text onto the screen
                    screen.blit(text, text_rect)
                    
                GreenTable.append(RowGreenRect)