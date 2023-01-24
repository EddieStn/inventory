# User Stories

## [#1 Create an account](https://github.com/EddieStn/inventory/issues/1)





# Bugs

* BUG: 
    * Every refresh resubmits form
    * fix:
        *   ```
            if request.method == 'POST':
                    if 'add_item' in request.POST:
                        add_item = ItemForm(request.POST)
                        if add_item.is_valid():
                            add_item.save()
                            return redirect('home') <!-- This line fixed the bug -->
            ```

* BUG:
    * All items created by other users would be saved for the superuser in the database
    * fix: 
        *   ```
            if 'add_item' in request.POST:
                add_item = ItemForm(request.user, request.POST)
                if add_item.is_valid():
                    add_item.instance.category = get_object_or_404(Category, name=request.POST.get('category'), user=request.user)
                    add_item.instance.user = request.user  <!-- This line fixed the bug -->
                    add_item.save()
            ```

# Credits 

* Search form is inspired from the Boutique-Ado project

# Acknowledgements

* Thanks to my mentor Chris Quinn for guidance
* Thanks to Code Institute tutors, for helping me with filtering, user-specific pages and bug fixes
* Thanks to Mounir for answering my [stack overflow post](https://stackoverflow.com/questions/75208985/handling-form-fields-in-django-for-logged-in-user)
* Thanks to Roman Rakic for discovering the bug in my code - [slack thread](https://code-institute-room.slack.com/archives/C026PTF46F5/p1673898571942309)