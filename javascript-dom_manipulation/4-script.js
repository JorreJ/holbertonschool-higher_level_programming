document.getElementById('add_item').addEventListener('click', function () {
  document.querySelector('.my_list').append(Object.assign(document.createElement('li'), { textContent: 'Item' }));
});
