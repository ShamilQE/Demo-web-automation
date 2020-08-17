
# 1. visit text box page
# 2. submit the form
# 3. assert something


def test_submit_form(py):
    py.visit('https://demoqa.com/text-box')
    py.get('#userName').type('Michael Thompson')
    py.get('#userEmail').type('example@demo.com')
    py.get('#currentAddress').type('101 State str SLC, 84xxx,  Utah')
    py.get('#permanentAddress').type('102 State str SLC, 84xxx,  Utah')
    py.get('#submit').click(force=True)
    output = py.get('#output')
    assert 'Michael Thompson' in output.text()
    assert 'example@demo.com' in output.text()
    assert '101 State str SLC, 84xxx,  Utah' in output.text()
    assert '102 State str SLC, 84xxx,  Utah' in output.text()


# REFACTORED
full_name = 'Michael Thompson'
email = 'example@demo.com'
c_address = '101 State str SLC, 84xxx, Utah'
p_address = '102 State str SLC, 84xxx, Utah'

def test_submit_form_refactored_001(py):
    py.visit('https://demoqa.com/text-box')

    py.get('#userName').type(full_name)
    py.get('#userEmail').type(email)
    py.get('#currentAddress').type(c_address)
    py.get('#permanentAddress').type(p_address)
    py.get('#submit').click(force=True)

    output = py.get('#output')
    assert full_name in output.text()
    assert email in output.text()
    assert c_address in output.text()
    assert p_address in output.text()










