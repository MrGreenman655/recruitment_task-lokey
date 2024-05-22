<template>
  <q-dialog v-model="modalData.isDialogOpen">
    <q-card style="width: 500px">
      <q-form @submit="editArticle" class="q-gutter-md q-pa-md">
        <q-card-section class="row justify-center">
          <q-avatar icon="edit" color="primary" text-color="white"/>
        </q-card-section>
        <q-card-section>
          <q-input
            v-model="modalData.title"
            :rules="[val => !!val || 'Field is required']"
            label="Title"/>
          <q-input
            label="Release date"
            v-model="modalData.release_date"
            mask="####-##-## ##:##:##"
            hint="####-##-## ##:##:##"
            :rules="[val => isValidDateOrEmpty(val) || 'This date notation is incorrect. It should be YYYY-MM-DD.']"
          />
          <q-input
            v-model="modalData.content"
            :rules="[val => !!val || 'Field is required']"
            type="textarea"
            label="Content"
          />
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="grey" v-close-popup/>
          <q-btn type="submit" flat label="Edit" color="primary"/>
        </q-card-actions>
      </q-form>
    </q-card>

  </q-dialog>
</template>

<script setup lang="ts">

import {reactive} from "vue";
import {api} from "boot/axios";
import {articleDetailEndpoint} from "src/api";
import {Notify} from "quasar";
import moment from "moment/moment";

const modalData: IModalData = reactive({
  article_id: '',
  title: '',
  content: '',
  release_date: '',
  isDialogOpen: false,
})

defineExpose({modalData})
const emits = defineEmits(['editDone'])

export interface IModalData {
  article_id: string
  title: string,
  content: string,
  release_date: string,
  isDialogOpen: boolean,
}

const editArticle = async () => {
  try {
    const formData = {title: modalData.title, content: modalData.content, release_date: modalData.release_date}
    await api.put(articleDetailEndpoint.replace('{article_id}', modalData.article_id), formData)
    Notify.create({message: 'Article has been edited.', color: "green"})
    modalData.isDialogOpen = false
    emits('editDone')
  } catch (e) {
    Notify.create({message: 'Failed to create article.', color: "negative"})
  }
}
const isValidDateOrEmpty = (date: string) => {
  if (date === '') {
    return true
  }
  return moment(date, 'YYYY-MM-DD HH:mm:ss', true).isValid();
}
</script>

<style scoped>

</style>
