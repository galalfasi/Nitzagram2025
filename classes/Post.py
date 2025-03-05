import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, loc, des, username):
        self.location = loc
        self.description = des
        self.username = username
        self.counter_likes = 0
        self.comments = []
        self.comments_display_index = 0

    def display(self):
        def display_above():
            position_index_user = (USER_NAME_X_POS,USER_NAME_Y_POS)
            position_index_loc = (LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS)
            position_index_des = (DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS)
            display_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            username_to_display = display_font.render(self.username,
                                                            True, LIGHT_GRAY)
            screen.blit(username_to_display, position_index_user)
            location_to_display = display_font.render(self.location,
                                                            True, LIGHT_GRAY)
            screen.blit(location_to_display, position_index_loc)
            description_to_display = display_font.render(self.description,
                                                            True, LIGHT_GRAY)
            screen.blit(description_to_display,position_index_des)


            



    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.counter_likes += 1

    def add_comments(self, text):
        self.comments.append(Comment(text))



class Comment:



