# Shakepay Python Interface
## _Fully functional replacement for the app_

### NOTE: The API is currently being reconstructed to follow proper python standards and work with the pip package manager. If you want to see the progress on this, checkout the V1 branch.

The module is designed to be as simple and flexible as possible, so most functions return raw values. All functions have DOCSTRINGS if you are confused on what they do, but most function are pretty self explanatory.

If you are interested in creating your own auth system instead of using the quick_auth function, look inside `shakepay_api/test.py` and `shakepay_api/authentication.py` for more information on how you should handle interaction.

## Examples

- `example_trigger_shackingsats.py` - authenticates the user and retrieves the shacking sats rewards
- `example_get_authentication.py` - authenticates the user and retrieves wallet information
- `example_send_cad.py` - authenticates the user and attempts to send 1$

The API will eventually be fully documented but I tried to make it as human friendly as possible if you do a little digging inside the files and look at the examples.

## Improvements

Feel free to create an issue if you believe an improvement could be made!

## Donate
You can tip me on Shakepay `@hammy5030`, Monero `83oauD72kHPhdWtPWb2rjvQpvSsPbrcBt5Z8UtrYx97A6ALqePB9QkNgMbuX1SMSbVSh9BxHB3KCUG6SBoZAjEvfNXgsLg9`
