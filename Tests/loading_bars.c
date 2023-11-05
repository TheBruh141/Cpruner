//
// Created by bruhpc on 10/27/23.
//

#include "loading_bars.h"
#include "allocators.h"
#include "common_bindings.h"

sml_status_bar
new_status(const char *name, const char *extra_info, float end_status, float status, enum Sml_Status_Type stat_type,enum Sml_Bar_Type bar_type ){
    sml_status_bar bar = {
            .status_type = stat_type,
            .bar_type = bar_type,
            .end_status = end_status,
            .name = name,
            .extra_info = extra_info
    };
    return bar;
}

// shows the status bar :D
// NOTE: does not support resizing the terminal :c
void sml_statusbar_show(sml_status_bar *bar, float bar_status, FILE *stream, char *message, ...){

    switch (bar->bar_type) {
        case loading:
            if (bar->bar_type == persentage){
                fprintf(stream, "loading[%d%%] ");
            } else
            {
                fprintf(stream, "[%d] ");
            }
            break;
        case status:
            break;
        case download:
            break;
        case fancy:
            break;
    }

}
void sml_bars_free_status(sml_status_bar *bar) {
    // Const to volatile. Blasphemy! :D
    free((char *) bar->name);
    free((char *) bar->extra_info);
}