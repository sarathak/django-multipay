from django.test import TestCase



class SampleTestCase(TestCase):
    def test_render_alert_without_type(self):
        self.assertEqual(
            render_alert("content"),
            (
                '<div class="alert alert-info alert-dismissible" role="alert">'
                '<button type="button" class="close" data-dismiss="alert" aria-label="close">&times;</button>content'
                "</div>"
            ),
        )
