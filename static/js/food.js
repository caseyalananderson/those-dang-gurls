 $(document).ready(function() {


      // fix menu when passed
      $('.masthead').visibility({
          once: false,
          onBottomPassed: function() {
            $('.fixed.menu').transition('fade in');
          },
          onBottomPassedReverse: function() {
            $('.fixed.menu').transition('fade out');
          }
        })
      ;

      // create sidebar and attach to menu open
      $('.ui.sidebar')
        .sidebar('attach events', '.toc.item')
      ;

      // toggle on the comment reply
      // $('.comment-reply-btn').click(function(){ alert('test');});
      $('.comment-reply-btn')
         .click(function(event) {
            alert('button pressed');
            event.preventDefault();
            $(this).parent().next('.comment-reply').fadeToggle();
         })
      ;
  }
  ;
