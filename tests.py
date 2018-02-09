import unittest
from urllib2 import URLError
from func import url_extract, html_parser


class ExtractorTests(unittest.TestCase):

    def test_consumers_output(self):
        url = 'http://www.pikselbit.com/projects/'
        expected_output = ['http://www.vinofino.rs']
        html = url_extract(url)
        output = html_parser(html)
        self.assertEqual(output, expected_output)

    def test_producers_incorrect_input(self):
        urls_list = ['ww.genmedica.rs','http://www.ecd.rs', 
                    'http:/www.google.com', 'http://www.vinofino.rs']
        with self.assertRaises(ValueError):
            url_extract(urls_list[0])
        with self.assertRaises(URLError):
            url_extract(urls_list[2])

#    def test_interruption_after_error(self):
#        urls_list = ['ww.genmedica.rs','http://www.ecd.rs', 
#                    'http:/www.google.com', 'http://www.vinofino.rs']
            
