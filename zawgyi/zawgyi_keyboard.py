#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#	You can always get the lastest version of this module at:
#
#	http://zawgyi-keyboard.googlecode.com/svn/branch/py-package/zawgyi
#
#	If that URL should fail, try contacting the author.
#
#	This zawgyi_keyboard module is maintained by Phone Htut <phonehtut2@gmail.com>.
#	If you find problem, please submit bug reports/patches via the zawgyi-keboard
#	project googlecode page and assign them to me. Thank you for your download.

""" 	zawgyi_keyboard.py module
	This module tries to help you get your fonts and xkb data on
	Linux/Unix system. It makes you easy install, remove, upgrade font.
"""
__author__ = "Phone Htut <phonehtut2@gmail.com>"
__copyright__ = "Copyright (c) 2009, Phone Htut"
__license__  = "GPLv3"


""" 	zawgyi-keyboard package """
__version__ = "0.3.0"
__metor__ = "box02 <thebox02@gmail.com>"

import os
import sys
import glob

#Classifying operating system paths, you can add other distro fhs.
class linux:
	fonts_dir = '/usr/share/fonts'
	data_dir = '/usr/share'
	doc_dir = '/usr/share/doc'
	xkb_dir = ['/usr/share/X11/xkb/symbols', '/etc/X11/xkb/symbols']
	apps_dir = '/usr/share/applications'
	icons_dir = '/usr/share/pixmaps'
	def __init__(self):
		""" Classifying Linux FHS """
		print "Using Linux FHS...\n"

class freebsd:
	fonts_dir = '/usr/local/lib/X11/fonts'
	data_dir = '/usr/local/share'
	doc_dir = '/usr/local/share/doc'
	xkb_dir = '/usr/local/share/X11/xkb/symbols'
	apps_dir = '/usr/local/share/applications'
	icons_dir = '/usr/local/share/pixmaps'
	def __init__(self):
		""" Classifying FreeBSD FHS """
		print "Using FreeBSD FHS...\n"


# Detecting distributions and finding correct paths for installation	
if sys.platform == 'linux2':
	print '\nYour system is running Linux'
	use_fhs = linux()
	possible_xkb_dirs = use_fhs.xkb_dir
	for correct_xkb_dir in possible_xkb_dirs:
		if os.path.exists(correct_xkb_dir):
			XKB_DIR = correct_xkb_dir
			break
	FONT_DIR = use_fhs.fonts_dir
	DATA_DIR = use_fhs.data_dir
	DOC_DIR = use_fhs.doc_dir
	APPS_DIR = use_fhs.apps_dir
	ICONS_DIR = use_fhs.icons_dir
elif sys.platform == 'freebsd7':
	print '\nYour system is running FreeBSD'
	use_fhs = freebsd()
	FONT_DIR = use_fhs.fonts_dir
	DATA_DIR = use_fhs.data_dir
	DOC_DIR = use_fhs.doc_dir
	XKB_DIR= use_fhs.xkb_dir
	APPS_DIR = use_fhs.apps_dir
	ICONS_DIR = use_fhs.icons_dir
# testing on windows xp
elif sys.platform == 'cygwin':
	print '\nYour system is running cygwin on Windows'
	use_fhs = linux()
	possible_xkb_dirs = use_fhs.xkb_dir
	for correct_xkb_dir in possible_xkb_dirs:
		if os.path.exists(correct_xkb_dir):
			XKB_DIR = correct_xkb_dir
			break
	FONT_DIR = use_fhs.fonts_dir
	DATA_DIR = use_fhs.data_dir
	DOC_DIR = use_fhs.doc_dir
	APPS_DIR = use_fhs.apps_dir
	ICONS_DIR = use_fhs.icons_dir
else:
	sys.exit('Sorry, please try on Linux/Unix system!\n')
	
# Checking source paths and source files
print 'Checking source files from the package...'
"""	Checking source files in your package if you distribute
	In order to work with this module, you might need to put your fonts, 
 	xkb symbols file and other files in src_path named src folder, 
 	otherwise you might have to declare your src_path.
 	for example:
		src_path = './src0/' and './src1'
		font_file = './src/?.ttf'
		xkb_data = './src/mm'
		map_file = './src/?.pdf or ?.png or ?.jpg'
		desktop_file = '/src/?.desktop'
		icon = './src/?.png'
		
"""
# my source folder and files here:
src_path_0 = './src0/'
src_path_1  = './src1/'
#font_file  = not define -- changeable
xkb_data = 'mm'
map1 = 'zawgyikeyboard.pdf'
map2 = 'zawgyi_keyboard_unicode5.1_style.png'
desktop_file = 'zawgyi.desktop'
icon = 'zawgyi.png'

# finding fonts
if os.path.exists(src_path_0):
	for src_font in os.listdir(src_path_0):
		if src_font.endswith('ttf'):
			src_font = os.path.join(src_path_0, src_font)
	 		print 'Font : %s [ OK ]' % src_font
			break
else:
	print 'error: Font not found.'
	sys.exit("Interrupted installation.\n")
	
# finding mm files
src_xkb_data = os.path.join(src_path_0, xkb_data)
if os.path.exists(src_xkb_data):
	xkb_data = open(src_xkb_data).read()
	if xkb_data.find('zawgyi') == -1:
		print 'error: You have NOT zawgyi mm file!'
	elif xkb_data.find('soemin@my-MM.org') == -1:
		print 'You have modified zawgyi mm file!'
	else:
		print 'New mm xkeyboard unicode style [ OK ]'
else:
	print 'error: mm xkeyboard file not found.'
	sys.exit("Interrupted installation.\n")

# finding keyboard map
src_map_path1 = os.path.join(src_path_0, map1)
src_map_path2 = os.path.join(src_path_0, map2)
src_map_paths = [src_map_path1, src_map_path2]
for correct_map_path in src_map_paths:
	if os.path.exists(correct_map_path):
		src_map_path = correct_map_path
		print 'Keyboard layout map [ OK ]'
		break
else:
	print 'error: Keyboard Layout map not found.'
# finding desktop file
if sys.platform == 'linux2':
	src_desktop = os.path.join(src_path_0, desktop_file)
	if os.path.exists(src_desktop):
		print 'Desktop file for Linux [ OK ]'
elif sys.platform == 'freebsd7':
	src_desktop = os.path.join(src_path_1, desktop_file)
	if os.path.exists(src_desktop):
		print 'Desktop file for FreeBSD [ OK ]'
elif sys.platform == 'cygwin':
	src_desktop = os.path.join(src_path_0, desktop_file)
	if os.path.exists(src_desktop):
		print 'Desktop file for Cygwin [ OK ]'
else:
	print 'Refusing to install desktop file on menu.'# finding icon file
src_icon = os.path.join(src_path_0, icon)
if os.path.exists(src_icon):
	print 'Icon [ OK ]\n'
else:
	print 'Icon not found.\n'
	
# Installation fonts and keyboard data
def install():
	""" Install font and xkeyboard data """
	# making directories 
	print 'Installing directories...'
	new_font_dir = os.path.join(FONT_DIR, FONTNAME)
	new_data_dir = os.path.join(DATA_DIR, FONTNAME)
	new_doc_dir = os.path.join(DOC_DIR, FONTNAME)
	os.mkdir(new_font_dir)
	os.mkdir(new_data_dir)
	os.mkdir(new_doc_dir)
	print 'Installing directories done.'

	# installing font file
	print 'Installing %s font...' % FONTNAME
	if os.path.exists(new_font_dir):
		os.system('cp %s %s' % (src_font, new_font_dir))
		print 'Installing %s font done.' % FONTNAME
	else:
		print 'error: Font not installed!'
	
	# backing up existing mm file
	print 'Backuping original mm xkb file...'
	mm_orig = os.path.join(XKB_DIR, 'mm')
	os.rename(mm_orig, mm_orig + '_bak')
	mm_bak = os.path.join(XKB_DIR, 'mm_bak')
	if os.path.exists(mm_bak):
		print 'Backuping original mm xkb file done.'
	else:
		print 'error: Not backup original xkb file!'
		
	# install zawgyi mm xkeyboard
	print 'Installing zawgyi xkeyboard...'		
	os.system('cp %s %s' % (src_xkb_data, XKB_DIR))
	mm_new = os.path.join(XKB_DIR, 'mm')
	if os.path.exists(mm_new):
		print 'Installing %s keyboard done.' % FONTNAME
	else:
		print 'error: Not install xkb!'
		
	# install zawgyi keymaps layout
	print 'Installing %s keymaps layout...' % FONTNAME
	os.system('cp %s %s' % (src_map_path, new_data_dir))
	new_map_path1 = os.path.join(new_data_dir, map1)
	new_map_path2 = os.path.join(new_data_dir, map2)	
	if os.path.exists(new_map_path1) or os.path.exists(new_map_path2):
		print 'Installing %s keymaps layout done.' % FONTNAME
	else:
		print 'error: Not install keymaps layout!'	
				
	# install desktop file
	os.system('cp %s %s' % (src_desktop, APPS_DIR))
	
	# install icon file
	os.system('cp %s %s' % (src_icon, ICONS_DIR))
	
	# install documents
	print 'Installing documents...'
	os.system('cp AUTHORS changelog COPYRIGHT %s' % (new_doc_dir))
	os.system('cp CREDITS NOTICE %s' % (new_doc_dir))
	print 'Installing documents done.'
	
# Removing fonts and keyboard data
def remove():
	""" Remove the installation files and data """
	# check and delete previous installed package 
	dest_font_dir = os.path.join(FONT_DIR, FONTNAME)
	dest_data_dir = os.path.join(DATA_DIR, FONTNAME)
	dest_doc_dir = os.path.join(DOC_DIR, FONTNAME)
	dest_desktop_file = os.path.join(APPS_DIR, FONTNAME + '.desktop')
	dest_icon = os.path.join(ICONS_DIR, FONTNAME + '.png')
	
	if os.path.exists(dest_font_dir):
		print 'Removing previous installed %s font directory...' % FONTNAME
		os.system('rm -rf ' + dest_font_dir)
	if os.path.exists(dest_data_dir):
		print 'Removing previous installed %s data directory...'  % FONTNAME
		os.system('rm -rf ' + dest_data_dir)
	if os.path.exists(dest_doc_dir):
		print 'Removing previous installed %s doc directory...' % FONTNAME
		os.system('rm -rf ' + dest_doc_dir)
	if os.path.exists(dest_desktop_file):
		print 'Removing previous installed %s desktop file...' % FONTNAME
		os.remove(dest_desktop_file)
	if os.path.exists(dest_icon):
		print 'Removing previous installed %s icon...' % FONTNAME
		os.remove(dest_icon)
	# restore origial or backup xkb_data file
	mm_backup = os.path.join(XKB_DIR, 'mm_bak')
	mm_original = os.path.join(XKB_DIR, 'mm')
	if os.path.exists(mm_backup):
		print 'Restoring mm backup file...'
		os.rename(mm_backup, mm_original)
		if os.path.exists(mm_original):
			print 'Restoring origianl or backup mm file done.'
		else:
			print 'error: Not restore from backup file!'
	else:
		print 'Skip Restoring backup file : You do not have a backup file.'
	print 'Previous package removal done successfully!\n'
	
# Post installation
def layout_help():
	""" Guiding after installation """
	print '''
	* Go to System > Preferences > Keyboard, click on Keyboard, then
	Keyboard Preferences Window would be appeared.
	* Go to Layout Tab and click on Add button. Choose a Layout Myanmar 
	and press Add button. You will have both US English Layout and 
	Myanmar Zawgyi Layout.
	
	* To get keyboard switching, press Layout Options in the Layout Tab 
	of Keyboard Preferences.
	* Check e.g. Shift+Ctrl Change Layout in Layout Switching.
	
	* To get Keyboard Indicator on your panel, right-click on Panel and 
	click on Add to Panel. Search Keyboard Indicator and click it to add. 
	You will see Keyboard Indicator on your Panel.

	NOTE:
	For old zawgyi font till ZawgyiOne20080210, it needs to have 
	Third Level Chooser.
	For new zawgyi font (from July 2009 version), it does not need 
	to have Third Level Chooser. It would be using shift+f instead of 
	pressing Third Level Switch Key. 
	
	TIPS:	
	To see Keyboard Layout map, go to Applications > System Tools > Zawgyi
	Keyboard.
'''

# New font updating if new updated font is released outside
def font_update():
	""" in case you want to update font if new updated font released  """
	print '''WARNING: You should have New zawgyi font downloaded and You have to show me
your path of directory where the new download font is. For example:
your font is in Destkop folder: so your path is /home/username/Desktop .

Do you want to do it?
'''
	while 1:
		b = raw_input('Press [y] yes | [n] no ? ')
		if b == 'y':
			a = raw_input('\nEnter your downloaded font directory : ')
			if os.path.exists(a):
				for get_font in os.listdir(a):
					if get_font.startswith('Zawgyi') and get_font.endswith('ttf'):
						get_font = os.path.join(a, get_font)
						print '\nYour new given font is %s' % get_font
						break
				cur_font = glob.glob(os.path.join(FONT_DIR, FONTNAME, '*.ttf'))
				print 'Current installed font is %s' % cur_font
				print '''\nPRECAUTION: Please be sure that your new font should be newer than
the old one. Otherwise your font and keyboard not functional!!!'''
				while 1:
					c = raw_input('\nDo you really need to upgrade ? y/n : ')
					if c == 'y':
						delete_font_dir = os.path.join(FONT_DIR, FONTNAME)
						if os.path.exists(delete_font_dir):
							os.system('rm -rf ' + delete_font_dir)
						upgrade_font_dir = os.path.join(FONT_DIR, FONTNAME)
						os.mkdir(upgrade_font_dir)
						if os.path.exists(upgrade_font_dir):
							os.system('cp %s %s ' % (get_font, upgrade_font_dir))
							print '\nUpdating font successfully done.\n'
						break
					elif c == 'n':
						print 'User considers no need to upgrade now.\n'
						break
					else:
						print '\nPlease press *small letter* [y] or [n] !'
				break
			else:
				print '\nerror: Not found your input directory!\n'
				break
		elif b == 'n':
			print '\nOK, it\'s  your choice.\n'
			break
		else:
			print '\nPlease press *small letter* [y] or [n] !\n'
				
					
if __name__ == '__main__':

	# Given font name, if you wish, you can change another font name.
	# Now the module name is zawgyi_keyboard.py so I give the fontname as: 
	FONTNAME = 'zawgyi'
	
	# asking what to do ( install or uninstall, something like that)
	print "You are about to press..."
	while 1:
		ans = raw_input('[i] install, [r] remove, [h] layout help, [u] update font, [q] exit : ')
		if ans == 'i':
			print '\nProceeding installation...\n'
			remove()
			install()
			print '''Installation is finished!\n
You may NEED to Log Out or Restart your system to correct your keyboard.\n'''

		elif ans == 'r':
			print '\nProceeding uninstallation...\n'
			remove()
		elif ans ==  'h':
			print '\nProceeding keyboard layout option help...\n'
			layout_help()
		elif ans == 'q':
			sys.exit('\nHave a nice day, Good bye!\n')
		elif ans == 'u':
			print '\nProceeding font updating...\n'
			font_update()
		else:
			print '\nPlease press *small letter* [i] [r] [h] [u] [q] ! \n'
		
