from features.system import open_system_settings, open_file_explorer
from features.applications import open_code_editor, open_notepad_editor, \
    open_calendar_app, search_anything, open_discord, open_facebook, open_github, start_google_meet, \
    open_command_prompt, open_calculator_app, open_default_browser, open_email_client, open_camera_app, \
    open_photo_viewer, open_maps_app, open_clock_app, check_weather, open_chrome_browser, open_chatgpt
from features.browser.google import open_google, search_on_google, open_google_docs, open_google_sheets
from features.browser.youtube import open_youtube, search_on_youtube, play_youtube_video, toggle_youtube_video

functions = {
    "open_chrome_browser": open_chrome_browser,
    "open_default_browser": open_chrome_browser,
    "open_chatgpt": open_chatgpt,
    "open_google": open_google,
    "search_on_google": search_on_google,
    "open_youtube": open_youtube,
    "search_on_youtube": search_on_youtube,
    "play_youtube_video": play_youtube_video,
    "pause_youtube_video": toggle_youtube_video,
    "resume_youtube_video": toggle_youtube_video,
    "search_anything": search_anything,
    "open_code_editor": open_code_editor,
    "open_discord": open_discord,
    "open_facebook": open_facebook,
    "start_google_meet": start_google_meet,
    "open_github": open_github,
    "open_file_explorer": open_file_explorer,
    "open_notepad_editor": open_notepad_editor,
    "open_calendar_app": open_calendar_app,
    "open_google_docs": open_google_docs,
    "open_google_sheets": open_google_sheets,
    "open_command_prompt": open_command_prompt,
    "open_calculator_app": open_calculator_app,
    "open_default_browser": open_default_browser,
    "open_email_client": open_email_client,
    "open_system_settings": open_system_settings,
    "open_camera_app": open_camera_app,
    "open_photo_viewer": open_photo_viewer,
    "open_maps_app": open_maps_app,
    "open_clock_app": open_clock_app,
    "check_weather": check_weather,
}