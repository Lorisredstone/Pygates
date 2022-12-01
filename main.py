from src.window import Window

# just a small window

window:Window = Window((600, 600))
window.mainloop()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
            # quit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 key_state[0] = True
#             if event.key == pygame.K_RIGHT:
#                 key_state[1] = True
#             if event.key == pygame.K_UP:
#                 key_state[2] = True
#             if event.key == pygame.K_DOWN:
#                 key_state[3] = True
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 key_state[0] = False
#             if event.key == pygame.K_RIGHT:
#                 key_state[1] = False
#             if event.key == pygame.K_UP:
#                 key_state[2] = False
#             if event.key == pygame.K_DOWN:
#                 key_state[3] = False
#     window_offset[0] += key_state[0] * -1
#     window_offset[0] += key_state[1] * 1
#     window_offset[1] += key_state[2] * -1
#     window_offset[1] += key_state[3] * 1

#     screen.fill((0, 0, 0))
    
    
    
#     pygame.display.flip()