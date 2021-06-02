
class ImdbLocators:
    # locators for releases
    releases_table = "//div[contains(@id, 'main')]/*"
    # locators for charts
    sort_dropdown = "//select[contains(@id, 'lister-sort-by-options')]/*"
    chart_table = "//table[contains(@class, 'chart')]/tbody/tr"
    # locators for title - alternative
    alt_title_name = "//h1[contains(@class, 'dxSWFG')]"  
    alt_subtitle = "//div[contains(@class, 'ipc-chip-list')]"  
    alt_release = "//div[contains(@class, 'gvoMeT')]"
    alt_title_image = "//div[contains(@class, 'ipc-poster--baseAlt')]/div[contains(@class, 'ipc-media')]/img"
    alt_trailer_link = "//a[contains(@class, 'fnVjFH')]"
    alt_trailer_image = "//div[contains(@class, 'eMOScz')]/div[contains(@class, 'ipc-media')]/img"
    alt_director = "//ul[contains(@class, 'jCTgXs')]/li" 
    alt_description = "//p[contains(@class, 'kmrpno')]"
    alt_cast_table = "//a[contains(@class, 'eyqFnv')]"
    # locators for title
    title_name = "//div[contains(@class, 'title_wrapper')]/h1" 
    subtitle = "//div[contains(@class, 'title_wrapper')]/div[contains(@class, 'subtext')]/a"
    title_image = "//div[contains(@class, 'poster')]/a/img"
    trailer_image = "//div[contains(@class, 'slate')]/a/img"
    trailer_link = "//div[contains(@class, 'slate')]/a"
    title_director = "//div[contains(@class, 'plot_summary')]"
    title_description = "//div[contains(@class, 'summary_text')]"
    cast_table = "//table[contains(@class, 'cast_list')]/tbody/tr[contains(@class, 'odd') or contains(@class, 'even')]"
    # locators for trailer
    trailer_duration = "//div[contains(@class, 'jw-text-duration')]"
    fullscreen_button = "//div[contains(@class, 'jw-icon-fullscreen')]"
    play_button = "//div[contains(@class, 'jw-icon-playback')]"

