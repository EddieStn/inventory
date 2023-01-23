# Bugs

* bug: 
    * every refresh resubmits form
* fix: added return redirect('home') after form.save()

    *   ```
        if request.method == 'POST':
                if 'add_item' in request.POST:
                    add_item = ItemForm(request.POST)
                    if add_item.is_valid():
                        add_item.save()
                        return redirect('home')
        ```
# Credits 

* Search form is inspired from the Boutique-Ado project

# Acknowledgements

* Thanks to my mentor Chris Quinn for guidance
* Thanks to Code Institute tutor Scott, for helping me with filtering and user-specific pages
* Thanks to Mounir for answering my [stack overflow post](https://stackoverflow.com/questions/75208985/handling-form-fields-in-django-for-logged-in-user)
* Thanks to Roman Rakic for discovering the bug in my code - [slack thread](https://code-institute-room.slack.com/archives/C026PTF46F5/p1673898571942309)