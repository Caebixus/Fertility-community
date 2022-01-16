if (localStorage.getItem('cookies') != 'shown') {
  $('.cookies-popup-banner').show();
  $('#cookiesModal').modal('show')
  localStorage.setItem('cookies','shown')
};
