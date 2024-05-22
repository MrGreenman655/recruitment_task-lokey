<template>
  <q-dialog v-model="modalData.isDialogOpen">
    <q-card style="width: 500px">
      <q-form @submit="createArticle" class="q-gutter-md q-pa-md">
        <q-card-section class="row justify-center">
          <q-avatar icon="add" color="green" text-color="white"/>
        </q-card-section>
        <q-card-section>
          <q-input
            label="Title"
            v-model="modalData.title"
            :rules="[val => !!val || 'Field is required']"
          />
          <q-input
            label="Release date"
            v-model="modalData.release_date"
            mask="####-##-## ##:##:##"
            hint="####-##-## ##:##:##"
            :rules="[val => isValidDateOrEmpty(val) || 'This date notation is incorrect. It should be YYYY-MM-DD.']"
          />
          <q-input
            label="Content"
            v-model="modalData.content"
            type="textarea"
            :rules="[val => !!val || 'Field is required']"
          />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="grey" v-close-popup/>
          <q-btn type="submit" flat label="Create" color="green"/>
        </q-card-actions>
      </q-form>
    </q-card>

  </q-dialog>
</template>

<script setup lang="ts">

import {reactive} from "vue";
import {api} from "boot/axios";
import {articleDetailEndpoint, articlesEndpoint} from "src/api";
import {date, Notify} from "quasar";
import moment from "moment";

const modalData: IModalData = reactive({
  title: '',
  content: '',
  release_date: '',
  isDialogOpen: false,
})

defineExpose({modalData})
const emits = defineEmits(['createDone'])

export interface IModalData {
  title: string,
  release_date: string,
  content: string,
  isDialogOpen: boolean,
}

const createArticle = async () => {
  try {
    const formData = {title: modalData.title, content: modalData.content, release_date: modalData.release_date}
    await api.post(articlesEndpoint, formData)
    Notify.create({message: 'Article has been created.', color: "green"})
    modalData.isDialogOpen = false
    emits('createDone')
  } catch (e) {
    Notify.create({message: 'Failed to create article.', color: "negative"})
  }
}
const isValidDateOrEmpty = (date: string) => {
  if(date==='') {
    return true
  }
  return moment(date, 'YYYY-MM-DD HH:mm:ss', true).isValid();
}
</script>

<style scoped>

</style>
