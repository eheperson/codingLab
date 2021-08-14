Programming Guide » Controlling the environment¶
Many environment variables are available to control the initialization and behavior of Kivy.

For example, in order to restrict text rendering to the PIL implementation:

$ KIVY_TEXT=pil python main.py
Environment variables should be set before importing kivy:

import os
os.environ['KIVY_TEXT'] = 'pil'
import kivy