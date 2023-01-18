bug: 
every refresh resubmits form
fix: added return redirect('home') after form.save()

```
if request.method == 'POST':
        if 'add_item' in request.POST:
            add_item = ItemForm(request.POST)
            if add_item.is_valid():
                add_item.save()
                return redirect('home')
```