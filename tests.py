import os
import unittest
import prune_files_and_folders
from string import count

class TestCasts(unittest.TestCase):
    
    def create_test_file(self, base_dir):
        filepath = os.path.join(base_dir, 'empty_text_file') 
        open(os.path.join(base_dir, 'empty_text_file'), 'a').close()
        
        return filepath
    
    
    def test_can_get_file_list(self):
        base_dir = os.path.join(str(os.getcwd()), 'testfiles')
        filelist = prune_files_and_folders.get_files(base_dir)
        
        self.assertEqual(2, len(filelist))
        
    def test_can_get_folder_list(self):
        base_dir = os.path.join(str(os.getcwd()), 'testfiles')
        dirlist = prune_files_and_folders.get_dirs(base_dir)
        
        self.assertEqual(3, len(dirlist))
    
    def test_can_get_list_of_outdated_files(self):
        self.fail("Not implemented")
    
    
    def test_can_delete_file(self):
        base_dir = os.path.join(str(os.getcwd()), 'testfiles', 'delete_file_tests')
        filepath = self.create_test_file(base_dir)
        prune_files_and_folders.delete_file(filepath)
        
        self.assertFalse(os.path.isfile(filepath), "File was not deleted")
        
    
if __name__ == "__main__":
    unittest.main()