// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#registrantTable').DataTable({
        "order": [[ 7, "desc" ]]
    });
  $('#carouselTable').DataTable();
  $("#paymentTable").DataTable();
  $("#aribaTable").DataTable();
  $("#descTable").DataTable();
});
