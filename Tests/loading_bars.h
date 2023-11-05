//
// Created by bruhpc on 10/27/23.
//

#ifndef SML_LIB_LOADING_BARS_H
#define SML_LIB_LOADING_BARS_H

#include <stdio.h>

enum Sml_Bar_Type {
    loading, status, download, fancy
};

enum Sml_Status_Type {
    persentage, number
};


typedef struct {
    const enum Sml_Bar_Type bar_type;
    const enum Sml_Status_Type status_type;
    const float end_status;
    const char *name;
    const char *extra_info;
} sml_status_bar;

sml_status_bar
new_status(const char *name, const char *extra_info, float end_status, float status, enum Sml_Status_Type stat_type,enum Sml_Bar_Type bar_type );

// prints the status bar
void sml_statusbar_show(sml_status_bar *bar, float bar_status, FILE *stream, char *message, ...);

#endif //SML_LIB_LOADING_BARS_H
